'''
Partner bootstrap code. This program is run initially to set up partner job metadata in farmbeats.
'''
# system imports
import os
import sys
import json

# local imports
from datahub_lib.framework.fb_api import FarmbeatsApi
from datahub_lib.conf.baseconfig import BaseConfig
from datahub_lib.framework.logger import Logger

LOG = Logger.get_logger()

class Bootstrap:

    # class constants
    WEATHER_MEASURE_KEY = "WeatherMeasureType"
    WEATHER_MEASURE_UNIT_KEY = "WeatherMeasureUnit"

    ADD_MEASURE_TYPES = "add_extended_measure_types"
    ADD_MEASURE_UNITS = "add_extended_measure_units"
    ADD_WEATHER_DATA_MODELS = "add_data_models"
    ADD_JOB_TYPES = "add_job_types"


    def __init__(self, config_file, end_point, function_url):
        '''
        Initialize the bootstrap object - this has the required methods 
        to parse the manifest and onboard the partner on to farmbeats
        '''
        self.fb_api = FarmbeatsApi(endpoint=end_point, function_url=function_url)
        with open(config_file, "r") as conf:
            file_content = conf.read()
            self.bootstrap_manifest = json.loads(file_content)


    def add_new_extended_measure_types(self):
        '''
        Adds the extended measure types mentioned in the bootstrap_manifest
        '''
        # get the types that already exist
        weather_types = self.fb_api.get_extended_type_api().extended_type_get_all(keys=[Bootstrap.WEATHER_MEASURE_KEY]).to_dict()
        type_id = weather_types["items"][0]["id"]
        weather_type_list = weather_types["items"][0]["value"]

        # get the types that need to be added
        types_to_be_added = self.bootstrap_manifest[Bootstrap.ADD_MEASURE_TYPES]

        # merge them 
        merged_types_list = list(set(weather_type_list + types_to_be_added))

        # update farmbeats with new list
        inp = {}
        inp["key"] = Bootstrap.WEATHER_MEASURE_KEY
        inp["value"] = merged_types_list
        self.fb_api.get_extended_type_api().extended_type_update(id=type_id, input=inp)

    
    def add_new_extended_measure_units(self):
        '''
        Adds the extended measure units mentioned in the bootstrap_manifest
        '''
        # get the units that already exist
        weather_units = self.fb_api.get_extended_type_api().extended_type_get_all(keys=[Bootstrap.WEATHER_MEASURE_UNIT_KEY]).to_dict()
        unit_id = weather_units["items"][0]["id"]
        weather_units_list = weather_units["items"][0]["value"]

        # get the units that need to be added
        units_to_be_added = self.bootstrap_manifest[Bootstrap.ADD_MEASURE_UNITS]

        # merge them
        merged_units_list = list(set(weather_units_list + units_to_be_added))

        # update farmbeats with new list
        inp = {}
        inp["key"] = Bootstrap.WEATHER_MEASURE_UNIT_KEY
        inp["Value"] = merged_units_list
        self.fb_api.get_extended_type_api().extended_type_update(id=unit_id, input=inp)


    def upsert_weather_data_models(self):
        '''
        Upserts the weather data models mentioned in the bootstrap_manifest
        '''
        # get the existing weather data models
        existing_weather_data_models = self.fb_api.get_weather_data_model_api().weather_data_model_get_all(includes=["WeatherMeasures", "Properties"]).to_dict()
        
        # get the weather data models to upsert
        partner_wsm_list = self.bootstrap_manifest[Bootstrap.ADD_WEATHER_DATA_MODELS]
        
        # for every weather station model in the manifest
        for weather_data_model in partner_wsm_list:
            existing_wsms = existing_weather_data_models["items"]
            found = False 
            if (len(existing_wsms) > 0):
                # if a matching name is found for the partner - update
                for wsm in existing_wsms:
                    if (wsm["name"] == weather_data_model["name"]):
                        wsm_id = wsm["id"]
                        # update
                        found = True
                        self.fb_api.get_weather_data_model_api().weather_data_model_update(id=wsm_id, input=weather_data_model)
            if (not found):
                # else insert 
                self.fb_api.get_weather_data_model_api().weather_data_model_create(input=weather_data_model)


    def upsert_job_types(self):
        '''
        Upserts the partner job types mentioned in the bootstrap_manifest
        '''
        # get the existing job types for this partner.
        existing_partner_job_types = self.fb_api.get_job_type_api().job_type_get_all(includes=["PipelineDetails", "Properties"]).to_dict()

        # get the job types to upsert
        partner_job_types = self.bootstrap_manifest[Bootstrap.ADD_JOB_TYPES]

        # for every job type in the manifest
        for job_type in partner_job_types:
            existing_job_types = existing_partner_job_types["items"]
            found = False
            if (len(existing_job_types) > 0):
                # if a matching name is found for the job type - update
                for existing_job_type in existing_job_types:
                    if (existing_job_type["name"] == job_type["name"]):
                        job_type_id = existing_job_type["id"]
                        # update
                        found = True
                        self.fb_api.get_job_type_api().job_type_update(id=job_type_id, input=job_type)
            if (not found):
                # else insert
                self.fb_api.get_job_type_api().job_type_create(input=job_type)


def run(config_file, end_point, function_url):
    
    # create the bootstrap object - that will bootstrap the partner
    LOG.info("Creating bootstrap object")
    bootstrap = Bootstrap(config_file=config_file, end_point=end_point, function_url=function_url)
    LOG.info("Successfully created bootstrap object")

    # add new extended measure types
    LOG.info("Adding the new measure types")
    bootstrap.add_new_extended_measure_types()
    LOG.info("Successfully added the new measure types")

    # add new measure units
    LOG.info("Adding the new measure units")
    bootstrap.add_new_extended_measure_units()
    LOG.info("Successfully added the new measure units") 

    # upsert the weather data models
    LOG.info("Upserting new weather data models")
    bootstrap.upsert_weather_data_models()
    LOG.info("Successfully upserted the weather data models")

    # upsert the job types
    LOG.info("Upserting the job types")
    bootstrap.upsert_job_types()
    LOG.info("Successfully upserted the job types")


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "bootstrap_manifest.json")
    run(config_file=file_path, end_point=sys.argv[1], function_url=sys.argv[2]) 
    
    
