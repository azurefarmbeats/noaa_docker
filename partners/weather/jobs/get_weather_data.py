# System imports
from absl import app
from absl import flags
from datetime import datetime
from dateutil import parser
import math
import numpy as np

# Local imports
from datahub_lib.framework.fb_api import FarmbeatsApi
from datahub_lib.conf.baseconfig import BaseConfig
from azureml.opendatasets import NoaaIsdWeather


# Define flags used by this module. Mandatory flags first
# NOTE: Add 'allow_override=True' if same flags are created in multiple modules with dependency
flags.DEFINE_string("farm_id", None, "This is optional and just for association")
flags.DEFINE_string("start_date", None, "Start date")
flags.DEFINE_string("end_date", None, "End date")
flags.DEFINE_string("latitude", None, "Latitude")
flags.DEFINE_string("longitude", None, "Longitude")
flags.DEFINE_string("weather_station_id", None, "User either provides lat long/weather station id")
flags.DEFINE_string("event_hub_connection_string", None, "The job outputs NOAA ISD data for the given date range to event hub")
flags.DEFINE_string("end_point",  None, "farmbeats api endpoint")
flags.DEFINE_string("function_url", None, "function_url")

# Shorthand for referring to flags
FLAGS = flags.FLAGS

class GetWeatherDataJob:
    '''
    Object to fetch ISD weather data from Azure open datasets (NOAA ISD)
    '''

    # class constants
    INT_MAX = 1e17
    INVALID_LAT_LON = 500

    
    def __init__(self):
        pass


    def get_weather_data(self, start_date, end_date, lat, lon):
        '''
        Gets the closest proximity weather data available for the given date range, 
        '''
        # get data for given date range.
        weather_data = self.__get_weather_data_for_date_range(start_date, end_date)

        # get the data into a pandas data frame, so we can filter and process
        weather_data_df = weather_data.to_pandas_dataframe()

        # out of the lat longs available get the nearest points
        (nearest_lat, nearest_lon) = self.__find_nearest_lat_longs_in_data(weather_data_df, lat, lon)

        # filter the data to this lat and lon
        filtered_weather_data = weather_data_df[(weather_data_df['latitude'] == nearest_lat) & (weather_data_df['longitude'] == nearest_lon)]

        # push the data to eventhub


    
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
    # TODO - if there is weather station id provided, get lat long from there OR, get from the flags.
    job.get_weather_data(start_date = FLAGS.start_date, end_date = FLAGS.end_date, lat=47.75, lon=96.85)


if __name__ == '__main__':
    app.run(main)
   

    

