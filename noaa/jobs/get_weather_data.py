# System imports
from absl import app
from absl import flags
from datetime import datetime
from dateutil import parser
import math
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


# Define flags used by this module. Mandatory flags first
# NOTE: Add 'allow_override=True' if same flags are created in multiple modules with dependency
flags.DEFINE_string("farm_id", None, "This is optional and just for association")
flags.DEFINE_string("start_date", None, "Start date")
flags.DEFINE_string("end_date", None, "End date")
flags.DEFINE_string("latitude", None, "Latitude")
flags.DEFINE_string("longitude", None, "Longitude")
flags.DEFINE_string("eventhub_connection_string", None, "The job outputs NOAA ISD data for the given date range to event hub")
flags.DEFINE_string("end_point",  None, "farmbeats api endpoint")
flags.DEFINE_string("get_access_token_url", None, "Azure function url to get the access token")
flags.DEFINE_string("eventhub_name", None, "Name of the eventhub to push data to")

# Shorthand for referring to flags
FLAGS = flags.FLAGS

LOG = Logger.get_logger()

class GetWeatherDataJob:
    '''
    Class to fetch ISD weather data from Azure open datasets (NOAA ISD)
    '''

    # class constants
    INT_MAX = 1e17
    INVALID_LAT_LON = 500
    WEATHER_STATION_MODEL_NAME = "noaa_isd"

    
    def __init__(self):
        self.fb_api = FarmbeatsApi(endpoint=FLAGS.end_point, function_url=FLAGS.get_access_token_url)


    def get_weather_data(self, start_date, end_date, lat, lon):
        '''
        Gets the closest proximity weather data available for the given date range, 
        '''
        # get data for given date range.
        LOG.info("Getting data for dates " + start_date + " to " + end_date)
        weather_data = self.__get_weather_data_for_date_range(start_date, end_date)
        LOG.info("Successfully got data for dates " + start_date + " to " + end_date)

        # get the data into a pandas data frame, so we can filter and process
        weather_data_df = weather_data.to_pandas_dataframe()

        # out of the lat longs available get the nearest points
        LOG.info("Finding the nearest latitude and longitude from the available data")
        (nearest_lat, nearest_lon) = self.__find_nearest_lat_longs_in_data(weather_data_df, lat, lon)
        LOG.info("nearest lat, lon: [" + str(nearest_lat) + "," + str(nearest_lon) + "]")

        # filter the data to this lat and lon
        LOG.info("Filtering the data to nearest lat, lon")
        filtered_weather_data = weather_data_df[(weather_data_df['latitude'] == nearest_lat) & (weather_data_df['longitude'] == nearest_lon)]
        LOG.info(filtered_weather_data)

        # push the data to eventhub
        LOG.info("Pushing data to eventhub")
        self.__push_weather_data_to_farmbeats(filtered_weather_data)
        LOG.info("Successfully pushed data")
    
    
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


    def __process_weather_data_for_tsi(self, weather_station_id, weather_data):
        '''
        Converts the weather data from Pandas data frame to that expected by TSI
        '''
        msgs = []
        msg = json.loads('''{
                                    "weatherstations": [
                                        {
                                        "id": "",
                                        "weatherdata": []
                                        }
                                    ]
                                }'''
                        )
        msg["weatherstations"][0]["id"] = weather_station_id        
        row_data = msg["weatherstations"][0]["weatherdata"]
        # iterrows gives (index, row) tuples rather than just rows.
        # so, throwing away the index and just getting the row.
        for _,row in weather_data.iterrows():
            row_data.append(self.__get_eventhub_format(row))
        msg["weatherstations"][0]["weatherdata"] = row_data
        msgs.append(json.dumps(msg))
        return msgs


    async def __send_to_eventhub(self, weather_station_id, weather_data):
        '''
        Sends weather data to eventhub
        '''
        # Create a producer client to send messages to the event hub.
        producer = EventHubProducerClient.from_connection_string(conn_str=FLAGS.eventhub_connection_string, 
                                                                 eventhub_name=FLAGS.eventhub_name)
        async with producer:
            event_data_batch = await producer.create_batch()
            # process the weather data and create the msgs 
            msgs = self.__process_weather_data_for_tsi(weather_station_id, weather_data)
            # Add events to the batch
            for msg in msgs:
                event_data_batch.add(EventData(msg))
            await producer.send_batch(event_data_batch)


    def __get_weather_station_model_id(self, name):
        '''
        returns the weather station model id, given the name
        '''
        wsms = self.fb_api.get_weather_station_model_api().weather_station_model_get_all(names=[name]).to_dict()
        if (wsms):
            return wsms["items"][0]["id"]
        else:
            # RAISE ERROR
            return "not_found"


    def __get_weather_station_id(self):
        '''
        checks if a weather station already exists for the location, 
        if yes -> returns it's id.
        Else, creates and returns the id.
        '''
        weather_stations = self.fb_api.get_weather_station_api().weather_station_get_all().to_dict()
        for ws in weather_stations["items"]:
            lat = ws["location"]["latitude"]
            lon = ws["location"]["longitude"]
            if (lat == FLAGS.latitude and lon == FLAGS.longitude):
                # Found! - weather station for the given location already exists
                return ws["id"]
        
        # doesn't exist - create weather station
        weather_station_payload = {}
        weather_station_payload["name"] = "NOAA_job_generated_ws_[" + FLAGS.latitude + "," + FLAGS.longitude + "]" 
        weather_station_payload["weatherStationModelId"] = self.__get_weather_station_model_id(name=GetWeatherDataJob.WEATHER_STATION_MODEL_NAME)
        weather_station_payload["location"] = { "latitude": FLAGS.latitude, "longitude": FLAGS.longitude}
        if (FLAGS.farm_id):
            weather_station_payload["farmid"] = FLAGS.farm_id
        res = self.fb_api.get_weather_station_api().weather_station_create(input=weather_station_payload).to_dict()
        return res["id"]
        
      
    def __push_weather_data_to_farmbeats(self, weather_data):
        '''
        Pushes weather data to farmbeats - ingests data
        '''
        weather_station_id = self.__get_weather_station_id()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__send_to_eventhub(weather_station_id, weather_data))

    
    def __haversine_distance(self, origin, destination):
        '''
        Returns the haversine distance between two points on a sphere
        '''
        lat1, lon1 = origin
        lat2, lon2 = destination
        radius = 6371 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d


    def __get_weather_data_for_date_range(self, start_date, end_date):
        '''
        Returns all the weather data for a given date range.
        '''
        start_date = parser.parse(FLAGS.start_date)
        end_date = parser.parse(FLAGS.end_date)
        return NoaaIsdWeather(start_date, end_date)


    def __find_nearest_lat_longs_in_data(self, weather_data_df, lat, lon):
        '''
        Returns all the nearest lat longs available in the data
        '''
        # for all the latitudes and longitudes in the dataset - find the closest to the lat,lon
        min_dist = GetWeatherDataJob.INT_MAX
        closest_lat = GetWeatherDataJob.INVALID_LAT_LON
        closest_lon = GetWeatherDataJob.INVALID_LAT_LON
        for _,row in weather_data_df.loc[:, ['latitude', 'longitude']].iterrows():
            dist = self.__haversine_distance((lat, lon), (row['latitude'], row['longitude']))
            if (dist < min_dist):
                min_dist = dist
                closest_lat = row['latitude']
                closest_lon = row['longitude']
        return (closest_lat, closest_lon)      


def main(argv):
    job = GetWeatherDataJob()
    # get weather data
    job.get_weather_data(start_date=FLAGS.start_date, end_date=FLAGS.end_date, lat=float(FLAGS.latitude), lon=float(FLAGS.longitude))


if __name__ == '__main__':
    app.run(main)
   

    

