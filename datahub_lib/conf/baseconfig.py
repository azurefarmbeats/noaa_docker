'''
Config information for data accelerator
'''
from os import path
import configparser
import json


class BaseConfig:
    '''
    This class contains the properties related to AgData resources
    '''
    def __init__(self, end_point:str, tenant_id:str, app_id:str, app_secret:str, app_identifier_uri:str=None):
        '''
        Set the properties of Azure Resources created part as of the deployment
        '''
        self.app_identifier_uri = app_identifier_uri or end_point
        self.tenant_id = tenant_id
        self.app_id = app_id
        self.app_client_secret = app_secret
        self.api_endpoint = end_point


    @staticmethod
    def from_config_file(config_file=None):
        '''
        Initializes object
        :param str config_file: Path to the config file
        '''
        # config.ini file contains all the azure resources names, secret names for this deployment
        default_config_path = '/mnt/batch/tasks/startup/wd/to_vm/config.ini'


        # ---------------------------------------------------------------------
        # Loading Top level resource names and their corresponding secrets (connection
        # strings or access-keys) in KeyVault from config.ini file.
        # ---------------------------------------------------------------------
        config_file = config_file or default_config_path
        '''
        Load the properties of Azure Resources created part of this deployment
        The properties are present in config.ini file present on batch nodes
        '''
        # Parse the config.ini file
        Config = configparser.ConfigParser()
        Config.read(config_file)

        # AAD app
        app_id = Config.get('aad_app', 'app_id')
        app_identifier_uri = Config.get('aad_app', 'identifier_uri')
        # TODO: expose get_aad_app_client_secret function instead of the app_client_secret property..
        app_client_secret = BaseConfig.__get_aad_app_client_secret(
            Config.get('aad_app', 'activity_json_file'))

        # Tenant Id
        tenant_id = Config.get('resource_group', 'tenant_id')

        # app service endpoint
        api_endpoint = Config.get('app_service', 'url')
        return BaseConfig(end_point=api_endpoint,
                          tenant_id=tenant_id,
                          app_id=app_id,
                          app_secret=app_client_secret,
                          app_identifier_uri=app_identifier_uri)


    @staticmethod
    def __get_aad_app_client_secret(activity_json_file):
        '''
        :param str config_file: Path to the 'activity.json' containing AAD App client secret
        :return: client_secret of the the AAD App
        '''
        # 'activity.json' Stores extendedProperties and properties of the custom activity.
        # Read 'aadAppClientSecret' propery value from activity.json file
        with open(activity_json_file, 'r') as f:
            customProperties = json.load(f)
        return customProperties["typeProperties"]["extendedProperties"]["aadAppClientSecret"]["value"]
