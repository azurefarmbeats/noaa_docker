# System imports
import sys
from absl import app
from absl import flags
from datetime import datetime, timedelta
from dateutil import parser
import math
import asyncio
import json
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from azureml.opendatasets import NoaaGfsWeatherV2
from datahub_lib.framework.logger import Logger
import time

# Local imports
from datahub_lib.framework.fb_api import FarmbeatsApi
from datahub_lib.conf.baseconfig import BaseConfig
from datahub_lib.framework.job_status_writer import JobStatusWriter
from datahub_lib.auth.partner_adf_helper import ExtendedPropertiesReader
from datahub_lib.framework.job_error import JobError
from noaa.jobs.utils import UtilFunctions
from noaa.jobs.constants import JobConstants


# Define flags used by this module.
# NOTE: Add 'allow_override=True' if same flags are created in multiple modules with dependency

# Parameters passed by user
flags.DEFINE_string("farm_id", None, "This is optional and just for association")
flags.DEFINE_string("start_date", None, "Start date")
flags.DEFINE_string("end_date", None, "End date")
flags.DEFINE_float("latitude", None, "Latitude")
flags.DEFINE_float("longitude", None, "Longitude")

# Parameters passed by the framework (farmbeats)
flags.DEFINE_string("eventhub_connection_string", None, "The job outputs NOAA GFS data for the given date range to event hub")
flags.DEFINE_string("end_point",  None, "farmbeats api endpoint")
flags.DEFINE_string("get_access_token_url", None, "Azure function url to get the access token")
flags.DEFINE_string("eventhub_name", None, "Name of the eventhub to push data to")
flags.DEFINE_string("job_status_blob_sas_url", None, "Job status blob url with sas token")

# Shorthand for referring to flags
FLAGS = flags.FLAGS

LOG = Logger.get_logger()

class GetWeatherForecastDataJob:
    '''
    Class to fetch GFS weather data from Azure open datasets (NOAA GFS)
    '''

    # class constants
    WEATHER_DATA_MODEL_NAME = "noaa_gfs"


    def __init__(self):
        self.adf_helper = ExtendedPropertiesReader()
        if (FLAGS.get_access_token_url is None):
            function_url = self.adf_helper.function_url
        else:
            function_url = FLAGS.get_access_token_url
        self.fb_api = FarmbeatsApi(endpoint=FLAGS.end_point, function_url=function_url)

        if (FLAGS.eventhub_connection_string is None):
            self.eventhub_connection_string = self.adf_helper.eventhub_connection_string
        else:
            self.eventhub_connection_string = FLAGS.eventhub_connection_string


    def __get_weather_forecast_data_for_day(self, day, lat, lon):
        '''
        Gets weather data for a given day and pushes it to eventhub
        '''
        try:
            # get data for given date range.
            start_time = time.time()
            LOG.info("Getting data for " + day.strftime("%m/%d/%Y, %H:%M:%S"))
            min_lat = min(lat - 1, -90)
            max_lat = max(lat + 1, 90)
            min_lon = min(lon - 1, -180)
            max_lon = max(lon + 1, 180)
            weather_data = NoaaGfsWeatherV2(start_date=day, end_date=day, min_latitude=min_lat, max_latitude=max_lat, min_longitude=min_lon, max_longitude=max_lon)
            LOG.info("Successfully got data for " + day.strftime("%m/%d/%Y, %H:%M:%S"))
            

            # get the data into a pandas data frame, so we can filter and process
            weather_data_df = weather_data.to_pandas_dataframe()
            LOG.info("Took {} seconds to get the data.".format(time.time() - start_time))

            # out of the lat longs available get the nearest points
            LOG.info("Finding the nearest latitude and longitude from the available data")
            (nearest_lat, nearest_lon) = UtilFunctions.find_nearest_lat_longs_in_data(weather_data_df, lat, lon)
            LOG.info("nearest lat, lon: [" + str(nearest_lat) + "," + str(nearest_lon) + "]")

            # filter the data to this lat and lon
            LOG.info("Filtering the data to nearest lat, lon")
            filtered_weather_data = weather_data_df[(weather_data_df['latitude'] == nearest_lat) & (weather_data_df['longitude'] == nearest_lon)]
            LOG.info(filtered_weather_data)

            # push the data to eventhub
            LOG.info("Pushing data to eventhub")
            wdl_id = self.__push_weather_data_to_farmbeats(filtered_weather_data)
            LOG.info("Successfully pushed data")

            # Update the status for the job
            if FLAGS.job_status_blob_sas_url:
                msg = "Weather data pushed for start_date: {} to end_date: {}\n for nearest_lat: {}, nearest_lon: {}\n provided lat:{}, lon:{}".format(
                    FLAGS.start_date, FLAGS.end_date, nearest_lat, nearest_lon, FLAGS.latitude, FLAGS.longitude)
                writer = JobStatusWriter(FLAGS.job_status_blob_sas_url)
                output_writer = writer.get_output_writer()
                output_writer.set_prop("WeatherDataLocationId: ", wdl_id)
                output_writer.set_prop("Message: ", msg)
                writer.set_success(True)
                writer.flush()


        except Exception as err:
            # Update the status in failure
            if FLAGS.job_status_blob_sas_url:
                writer = JobStatusWriter(FLAGS.job_status_blob_sas_url)
                writer.set_success(False)
                writer.flush()
            raise JobError(str(err), JobConstants.INTERNAL_ERROR, False)
                

    def __push_weather_data_to_farmbeats(self, weather_data):
        '''
        Pushes weather data to farmbeats - ingests data
        '''
        weather_data_location_id = self.__get_weather_data_location_id()
        LOG.info("Weather data location id: {}".format(weather_data_location_id))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__send_to_eventhub(weather_data_location_id, weather_data))
        return weather_data_location_id


    async def __send_to_eventhub(self, weather_data_location_id, weather_data):
        '''
        Sends weather data to eventhub
        '''
        # Create a producer client to send messages to the event hub.
        producer = EventHubProducerClient.from_connection_string(conn_str=self.eventhub_connection_string, 
                                                                 eventhub_name=FLAGS.eventhub_name)
        async with producer:
            event_data_batch = await producer.create_batch()
            # process the weather data and create the msgs 
            msgs = self.__process_weather_data_for_tsi(weather_data_location_id, weather_data)
            # Add events to the batch
            for msg in msgs:
                event_data_batch.add(EventData(msg))
            await producer.send_batch(event_data_batch)



    def __get_eventhub_format(self, row):
        '''
        Convert the data to a format that can be pushed to eventhub, which can be subsequently read by TSI
        '''
        output = {}  
        # get the timestamp
        forecastTimestamp = row["currentDatetime"] + timedelta(hours=row["forecastHour"])
        output["timestamp"] = forecastTimestamp.isoformat()
        output["predictiontimestamp"] = row["currentDatetime"].isoformat()
        output["Precipitation"] = row["precipitableWaterEntireAtmosphere"]
        output["SeaLvlPressure"] = row["seaLvlPressure"]
        output["AmbientTemperature"] = row["temperature"]
        output["CloudCover"] = row["totalCloudCoverConvectiveCloud"]
        output["WindSpeed"] = row["windSpeedGustSurface"]
        return output


    def __process_weather_data_for_tsi(self, weather_data_location_id, weather_data):
        '''
        Converts the weather data from Pandas data frame to that expected by TSI
        '''
        msgs = []
        msg = json.loads(JobConstants.WEATHER_TELEMETRY_FORMAT)
        msg[JobConstants.WEATHER_DATA_LOCATIONS][0][JobConstants.ID] = weather_data_location_id        
        row_data = msg[JobConstants.WEATHER_DATA_LOCATIONS][0][JobConstants.WEATHER_DATA]
        # iterrows gives (index, row) tuples rather than just rows.
        # so, throwing away the index and just getting the row.
        for _,row in weather_data.iterrows():
            row_data.append(self.__get_eventhub_format(row))
        msg[JobConstants.WEATHER_DATA_LOCATIONS][0][JobConstants.WEATHER_DATA] = row_data
        LOG.info("Pushing to eventhub:\n{}".format(json.dumps(msg)))
        msgs.append(json.dumps(msg))
        LOG.info("Event hub msg: {}".format(json.dumps(msg)))
        return msgs


    def __get_weather_data_location_id(self):
        '''
        checks if a weather data location already exists for the location, 
        if yes -> returns it's id.
        Else, creates and returns the id.
        '''
        data_model_id = self.__get_weather_data_model_id(name=GetWeatherForecastDataJob.WEATHER_DATA_MODEL_NAME)
        weather_data_locations = self.fb_api.get_weather_data_location_api().weather_data_location_get_all().to_dict()
        for loc in weather_data_locations[JobConstants.ITEMS]:
            lat = loc[JobConstants.LOCATION][JobConstants.LATITUDE]
            lon = loc[JobConstants.LOCATION][JobConstants.LONGITUDE]
            if (lat == FLAGS.latitude and lon == FLAGS.longitude and data_model_id == loc[JobConstants.WEATHER_DATA_MODEL_ID]):
                # Found! - weather data location for the given location already exists
                return loc[JobConstants.ID]
        
        # doesn't exist - create weather data_location
        weather_data_location_payload = {}
        weather_data_location_payload[JobConstants.NAME] = "NOAA_GFS_job_generated_location_[" + str(FLAGS.latitude) + "," + str(FLAGS.longitude) + "]" 
        weather_data_location_payload[JobConstants.WEATHER_DATA_MODEL_ID_PAYLOAD] = data_model_id
        weather_data_location_payload[JobConstants.LOCATION] = { JobConstants.LATITUDE: FLAGS.latitude, JobConstants.LONGITUDE: FLAGS.longitude}
        if (FLAGS.farm_id):
            weather_data_location_payload[JobConstants.FARM_ID] = FLAGS.farm_id
        res = self.fb_api.get_weather_data_location_api().weather_data_location_create(input=weather_data_location_payload).to_dict()
        return res[JobConstants.ID]


    def __get_weather_data_model_id(self, name):
        '''
        returns the weather data model id, given the name
        '''
        wsms = self.fb_api.get_weather_data_model_api().weather_data_model_get_all(names=[name], includes=[JobConstants.WEATHER_MEASURES, JobConstants.PROPERTIES]).to_dict()
        if (wsms):
            return wsms[JobConstants.ITEMS][0][JobConstants.ID]
        else:
            raise JobError("weather data model {} not found!".format(wsms), JobConstants.INTERNAL_ERROR, False)



    def get_weather_forecast_data(self, start_date, end_date, lat, lon):
        '''
        Gets the closest proximity weather data available for the given date range, 
        '''
        start_date = parser.parse(FLAGS.start_date)
        end_date = parser.parse(FLAGS.end_date)
        for day in UtilFunctions.daterange(start_date, end_date):
            self.__get_weather_forecast_data_for_day(day, lat, lon)



def main(argv):
    try:
        job = GetWeatherForecastDataJob()
        lat = float(FLAGS.latitude)
        lon = float(FLAGS.longitude)
        UtilFunctions.validate_lat_lon(lat, lon)
        # get weather forecast data
        job.get_weather_forecast_data(start_date=FLAGS.start_date, end_date=FLAGS.end_date, lat=lat, lon=lon)
    except Exception as err:
        if FLAGS.job_status_blob_sas_url:
            writer = JobStatusWriter(FLAGS.job_status_blob_sas_url)
            writer.set_success(False)
            writer.flush()
            JobError.write_to_status_file(err, FLAGS.job_status_blob_sas_url)
            sys.exit(1)


if __name__ == '__main__':
    app.run(main)
   
