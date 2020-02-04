# System imports
import os

# Local imports
from datahub_lib.swagger_client.configuration import Configuration
from datahub_lib.swagger_client.api_client import ApiClient

# import all the apis
from datahub_lib.framework.logger import Logger
from datahub_lib.swagger_client.api.alert_api import AlertApi
from datahub_lib.swagger_client.api.device_api import DeviceApi
from datahub_lib.swagger_client.api.device_model_api import DeviceModelApi
from datahub_lib.swagger_client.api.extended_type_api import ExtendedTypeApi
from datahub_lib.swagger_client.api.farm_api import FarmApi
from datahub_lib.swagger_client.api.job_api import JobApi
from datahub_lib.swagger_client.api.job_type_api import JobTypeApi
from datahub_lib.swagger_client.api.role_assignment_api import RoleAssignmentApi
from datahub_lib.swagger_client.api.role_definition_api import RoleDefinitionApi
from datahub_lib.swagger_client.api.rule_api import RuleApi
from datahub_lib.swagger_client.api.scene_api import SceneApi
from datahub_lib.swagger_client.api.scene_file_api import SceneFileApi
from datahub_lib.swagger_client.api.sensor_api import SensorApi
from datahub_lib.swagger_client.api.sensor_model_api import SensorModelApi
from datahub_lib.swagger_client.api.telemetry_api import TelemetryApi
from datahub_lib.swagger_client.api.weather_station_api import WeatherStationApi
from datahub_lib.swagger_client.api.weather_station_model_api import WeatherStationModelApi

from datahub_lib.auth.fb_auth_helper import FarmbeatsAuthHelper
from datahub_lib.auth.partner_auth_helper import PartnerAuthHelper
from datahub_lib.framework.constants import Constants
from datahub_lib.conf.baseconfig import BaseConfig

LOG = Logger.get_logger()

class FarmbeatsApi:
    '''
    Class to set configuration and get API objects for the various farmbeats datahub APIs.
    This class is not thread safe.
    '''
    def __init__(self, config:BaseConfig=None, endpoint:str=None, function_url:str=None):
        self.configuration = Configuration()
        self.partner_mode = False
        if config:
            # initialize the configuration
            self.configuration.host = config.api_endpoint
            self.auth_helper = FarmbeatsAuthHelper(api_endpoint = config.app_identifier_uri,
                tenant_id = config.tenant_id, app_id = config.app_id,
                app_client_secret = config.app_client_secret)
        else: # initialize with endpoint and function_url
            if endpoint is None or function_url is None: 
                raise ValueError("endpoint and function_url must be provided.")
            self.configuration.host = endpoint
            self.function_url = function_url
            self.auth_helper = PartnerAuthHelper(function_url)
            self.partner_mode = True
    

    def __authenticate(self):
        self.configuration.api_key_prefix[Constants.AUTHORIZATION] = Constants.BEARER
        if (self.partner_mode):
            self.configuration.api_key[Constants.AUTHORIZATION] = self.auth_helper.get_access_token()
        else:
            self.configuration.api_key[Constants.AUTHORIZATION] = self.auth_helper.get_access_token()[Constants.ACCESS_TOKEN]
        

    def get_alert_api(self):
        self.__authenticate()
        return AlertApi(ApiClient(self.configuration))


    def get_device_api(self):
        self.__authenticate()
        return DeviceApi(ApiClient(self.configuration))
    
    def get_device_model_api(self):
        self.__authenticate()
        return DeviceModelApi(ApiClient(self.configuration))
    
    
    def get_extended_type_api(self):
        self.__authenticate()
        return ExtendedTypeApi(ApiClient(self.configuration))
    

    def get_farm_api(self):
        self.__authenticate()
        return FarmApi(ApiClient(self.configuration))
    

    def get_job_api(self):
        self.__authenticate()
        return JobApi(ApiClient(self.configuration))
    

    def get_job_type_api(self):
        self.__authenticate()
        return JobTypeApi(ApiClient(self.configuration))
    

    def get_role_assignment_api(self):
        self.__authenticate()
        return RoleAssignmentApi(ApiClient(self.configuration))
        
        
    def get_role_definition_api(self):    
        self.__authenticate()
        return RoleDefinitionApi(ApiClient(self.configuration))
    

    def get_rule_api(self):
        self.__authenticate()
        return RuleApi(ApiClient(self.configuration))
        
        
    def get_scene_api(self):    
        self.__authenticate()
        return SceneApi(ApiClient(self.configuration))


    def get_scene_file_api(self):    
        self.__authenticate()
        return SceneFileApi(ApiClient(self.configuration))


    def get_sensor_api(self):
        self.__authenticate()
        return SensorApi(ApiClient(self.configuration))


    def get_sensor_model_api(self):
        self.__authenticate()
        return SensorModelApi(ApiClient(self.configuration))


    def get_telemetry_api(self):
        self.__authenticate()
        return TelemetryApi(ApiClient(self.configuration))


    def get_weather_station_api(self):
        self.__authenticate()
        return WeatherStationApi(ApiClient(self.configuration))

    
    def get_weather_station_model_api(self):
        self.__authenticate()
        return WeatherStationModelApi(ApiClient(self.configuration))

