# system imports
import os
import adal
import time
from datetime import datetime 

from datahub_lib.framework.logger import Logger
from datahub_lib.auth.authentication_helper import AuthenticationHelper

LOG = Logger.get_logger()

class PartnerAuthHelper(AuthenticationHelper):
    '''
    class that gets and manages the partner access token 
    '''
    def __init__(self, function_url:str):
        AuthenticationHelper.__init__(self)
        self.function_code = function_url


    def get_access_token(self):
        '''
        Generates the access token and returns it.
        :rtype: dict
        '''
        # TODO: call azure function to get the access token.
        pass

