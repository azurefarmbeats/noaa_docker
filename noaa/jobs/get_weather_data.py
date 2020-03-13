# System imports
from absl import app
from absl import flags
from datetime import datetime
from dateutil import parser

import asyncio
import json
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from azureml.opendatasets import NoaaIsdWeather
from datetime import datetime
from datahub_lib.framework.logger import Logger

# Local imports
from datahub_lib.framework.fb_api import FarmbeatsApi
from datahub_lib.conf.baseconfig import BaseConfig
from datahub_lib.framework.job_status_writer import JobStatusWriter
from datahub_lib.auth.partner_adf_helper import ExtendedPropertiesReader
from noaa.jobs.utils import UtilFunctions


# Define flags used by this module.
# NOTE: Add 'allow_override=True' if same flags are created in multiple modules with dependency

# Parameters passed by user
flags.DEFINE_string("farm_id", None, "This is optional and just for association")
flags.DEFINE_string("start_date", None, "Start date")
flags.DEFINE_string("end_date", None, "End date")
flags.DEFINE_string("latitude", None, "Latitude")
flags.DEFINE_string("longitude", None, "Longitude")

# Parameters passed by the framework (farmbeats)
flags.DEFINE_string("eventhub_connection_string", None, "The job outputs NOAA ISD data for the given date range to event hub")
flags.DEFINE_string("end_point",  None, "farmbeats api endpoint")
flags.DEFINE_string("get_access_token_url", None, "Azure function url to get the access token")
flags.DEFINE_string("eventhub_name", None, "Name of the eventhub to push data to")
flags.DEFINE_string("job_status_url", None, "Job status blob url with sas token")

# Shorthand for referring to flags
FLAGS = flags.FLAGS

LOG = Logger.get_logger()


class GetWeatherDataJob:
    '''
    Class to fetch ISD weather data from Azure open datasets (NOAA ISD)
    '''

    #class constants
    WEATHER_DATA_MODEL_NAME = "noaa_isd"

    
    def __init__(self):
        '''
        Constructor for GetWeatherDataJob
        '''
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



    def __get_weather_data_for_day(self, day, lat, lon):
        '''
        Gets weather data for a given day and pushes it to eventhub
        '''
        try:
            # get data for given date range.
            LOG.info("Getting data for " + day.strftime("%m/%d/%Y, %H:%M:%S"))
            weather_data = NoaaIsdWeather(day, day)
            LOG.info("Successfully got data for " + day.strftime("%m/%d/%Y, %H:%M:%S"))

            # get the data into a pandas data frame, so we can filter and process
            weather_data_df = weather_data.to_pandas_dataframe()

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
            self.__push_weather_data_to_farmbeats(filtered_weather_data)
            LOG.info("Successfully pushed data")

            # Update the status for the job
            if FLAGS.job_status_url:
                msg = "Weather data pushed for start_date: {} to end_date: {}, for nearest_lat: {}, nearest_lon: {}; provided lat:{}, lon{}".format(
                    FLAGS.start_date, FLAGS.end_date, nearest_lat, nearest_lon, FLAGS.latitude, FLAGS.longitude)
                writer = JobStatusWriter(FLAGS.job_status_url)
                output_writer = writer.get_output_writer()
                output_writer.set_prop("msg", msg)
                writer.set_success(True)
                writer.flush()

        except Exception as err:
            # Update the status in failure
            if FLAGS.job_status_url:
                writer = JobStatusWriter(FLAGS.job_status_url)
                writer.set_error('001', str(err), False)
                writer.set_success(False)
                writer.flush()


    def get_weather_data(self, start_date, end_date, lat, lon):
        '''
        Gets the closest proximity weather data available for the given date range, 
        '''
        start_date = parser.parse(FLAGS.start_date)
        end_date = parser.parse(FLAGS.end_date)
        for day in UtilFunctions.daterange(start_date, end_date):
            self.__get_weather_data_for_day(day, lat, lon)
        
    
    def __get_eventhub_format(self, row):
        '''
        Convert the data to a format that can be pushed to eventhub, which can be subsequently read by TSI
        '''
        output = {}
        # get the timestamp
        output["timestamp"] = row["datetime"].isoformat()
        output["Elevation"] = row["elevation"]
        output["WindAngle"] = row["windAngle"]
        output["AmbientTemperature"] = row["temperature"]
        output["SeaLvlPressure"] = row["seaLvlPressure"]
        output["PrecipTime"] = row["precipTime"]
        output["PrecipDepth"] = row["precipDepth"]
        output["SnowDepth"] = row["snowDepth"]
        return output


    def __process_weather_data_for_tsi(self, weather_data_location_id, weather_data):
        '''
        Converts the weather data from Pandas data frame to that expected by TSI
        '''
        msgs = []
        msg = json.loads('''{
                                    "weatherdatalocations": [
                                        {
                                        "id": "",
                                        "weatherdata": []
                                        }
                                    ]
                                }'''
                        )
        msg["weatherdatalocations"][0]["id"] = weather_data_location_id        
        row_data = msg["weatherdatalocations"][0]["weatherdata"]
        # iterrows gives (index, row) tuples rather than just rows.
        # so, throwing away the index and just getting the row.
        for _,row in weather_data.iterrows():
            row_data.append(self.__get_eventhub_format(row))
        msg["weatherdatalocations"][0]["weatherdata"] = row_data
        msgs.append(json.dumps(msg))
        return msgs


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


    def __get_weather_data_model_id(self, name):
        '''
        returns the weather data model id, given the name
        '''
        wsms = self.fb_api.get_weather_data_model_api().weather_data_model_get_all(names=[name]).to_dict()
        if (wsms):
            return wsms["items"][0]["id"]
        else:
            # RAISE ERROR
            return "not_found"


    def __get_weather_data_location_id(self):
        '''
        checks if a weather data location already exists for the location, 
        if yes -> returns it's id.
        Else, creates and returns the id.
        '''
        weather_data_locations = self.fb_api.get_weather_data_location_api().weather_data_location_get_all().to_dict()
        for loc in weather_data_locations["items"]:
            lat = loc["location"]["latitude"]
            lon = loc["location"]["longitude"]
            if (lat == float(FLAGS.latitude)and lon == float(FLAGS.longitude)):
                # Found! - weather data location for the given location already exists
                return loc["id"]
        
        # doesn't exist - create weather data_location
        weather_data_location_payload = {}
        weather_data_location_payload["name"] = "NOAA_job_generated_location_[" + FLAGS.latitude + "," + FLAGS.longitude + "]" 
        weather_data_location_payload["weatherDataModelId"] = self.__get_weather_data_model_id(name=GetWeatherDataJob.WEATHER_DATA_MODEL_NAME)
        weather_data_location_payload["location"] = { "latitude": FLAGS.latitude, "longitude": FLAGS.longitude}
        if (FLAGS.farm_id):
            weather_data_location_payload["farmid"] = FLAGS.farm_id
        res = self.fb_api.get_weather_data_location_api().weather_data_location_create(input=weather_data_location_payload).to_dict()
        return res["id"]
        
      
    def __push_weather_data_to_farmbeats(self, weather_data):
        '''
        Pushes weather data to farmbeats - ingests data
        '''
        weather_data_location_id = self.__get_weather_data_location_id()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__send_to_eventhub(weather_data_location_id, weather_data))

    
def main(argv):
    job = GetWeatherDataJob()
    # get weather data
    job.get_weather_data(start_date=FLAGS.start_date, end_date=FLAGS.end_date, lat=float(FLAGS.latitude), lon=float(FLAGS.longitude))


if __name__ == '__main__':
    app.run(main)
   

    

