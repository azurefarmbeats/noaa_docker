# system imports
import os
import adal
import time
from datetime import datetime 
import requests

from datahub_lib.framework.logger import Logger
from datahub_lib.auth.authentication_helper import AuthenticationHelper

LOG = Logger.get_logger()

class PartnerAuthHelper(AuthenticationHelper):
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

