from datetime import timedelta, date
from datahub_lib.framework.job_error import JobError
import math

class UtilFunctions:
    '''
    class to host the various utils required to run the jobs
    '''

    # class constants
    INT_MAX = 1e17
    INVALID_LAT_LON = 500
    
    
    def __init__(self):
        pass

    
    @staticmethod
    def daterange(start_date, end_date):
        '''
        Generator to give one day at a time.
        '''
        if (start_date > end_date):
            raise JobError("Bad request: Please ensure that start_date is prior to end_date", '400', False)
    
        for n in range(int ((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)


    @staticmethod
    def haversine_distance(origin, destination):
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

    
    @staticmethod
    def find_nearest_lat_longs_in_data(weather_data_df, lat, lon):
        '''
        Returns all the nearest lat longs available in the data
        '''
        # for all the latitudes and longitudes in the dataset - find the closest to the lat,lon
        min_dist = UtilFunctions.INT_MAX
        closest_lat = UtilFunctions.INVALID_LAT_LON
        closest_lon = UtilFunctions.INVALID_LAT_LON
        filtered_frame = weather_data_df.loc[:, ['latitude', 'longitude']].drop_duplicates() 
        for _,row in filtered_frame.iterrows():
            dist = UtilFunctions.haversine_distance((lat, lon), (row['latitude'], row['longitude']))
            if (dist < min_dist):
                min_dist = dist
                closest_lat = row['latitude']
                closest_lon = row['longitude']
        return (closest_lat, closest_lon)      