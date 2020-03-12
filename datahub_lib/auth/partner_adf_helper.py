import json

class ExtendedPropertiesReader:
    ACTIVITY_JSON_FILE_PATH = "/mnt/working_dir/activity.json"

    '''
    In ADF pipeline for job, we are passing some secure values as extended properties.
    '''
    def __init__(self):
        self.partner_creds = self.__get_partner_credentials()
        self.function_url = self.__get_function_url()
        self.eventhub_connection_string = self.__get_eventhub_connection_string()


    def __get_partner_credentials(self):
        '''
        Returns the partner credentials dict.
        :rtype: dict
        '''
        with open(ExtendedPropertiesReader.ACTIVITY_JSON_FILE_PATH, 'r') as f:
            customProperties = json.load(f)
            partnerCreds = customProperties["typeProperties"]["extendedProperties"]["partnerCredentials"]["value"]
            return json.loads(partnerCreds)


    def __get_function_url(self):
        '''
        Returns the azure function url passed in extended properties.
        '''
        with open(ExtendedPropertiesReader.ACTIVITY_JSON_FILE_PATH, 'r') as f:
            customProperties = json.load(f)
            function_url = customProperties["typeProperties"]["extendedProperties"]["partnerAccessTokenApiUrl"]["value"]
            return function_url


    def __get_eventhub_connection_string(self):
        '''
        Returns the azure function url passed in extended properties.
        '''
        with open(ExtendedPropertiesReader.ACTIVITY_JSON_FILE_PATH, 'r') as f:
            customProperties = json.load(f)
            function_url = customProperties["typeProperties"]["extendedProperties"]["eventHubConnectionString"]["value"]
            return function_url