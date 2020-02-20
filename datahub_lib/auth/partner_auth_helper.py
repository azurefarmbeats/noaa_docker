# system imports
import os
import adal
import time
from datetime import datetime 
import requests
import json

from datahub_lib.framework.logger import Logger
from datahub_lib.auth.authentication_helper import AuthenticationHelper

LOG = Logger.get_logger()

class PartnerAuthHelper(AuthenticationHelper):

    ACTIVITY_JSON_FILE_PATH = "/mnt/working_dir/activity.json"
    
    '''
    class that gets and manages the partner access token 
    '''
    def __init__(self, function_url:str):
        AuthenticationHelper.__init__(self)
        self.function_url = function_url


    def get_access_token(self):
        '''
        Generates the access token and returns it.
        :rtype: dict
        '''
        retry_count = 0
        while (retry_count < 3):
            res = requests.get(url=self.function_url)
            if (res.status_code == 200):
                return res.text
        LOG.error("Couldn't get valid access token!")


    def get_partner_credentials(self):
        '''
        Returns the partner credentials dict.
        :rtype: dict
        '''
        with open(PartnerAuthHelper.ACTIVITY_JSON_FILE_PATH, 'r') as f:
            customProperties = json.load(f)
            partnerCreds = customProperties["typeProperties"]["extendedProperties"]["partnerCredentials"]["value"]
            return json.loads(partnerCreds)
