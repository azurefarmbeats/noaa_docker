'''
This module generates and manages bearer auth token required to make API calls.
'''

# system imports
import os
import adal
import time
from datetime import datetime 

# local imports
from datahub_lib.framework.logger import Logger
LOG = Logger.get_logger()

class AuthenticationHelper:
    '''
    class that generates the bearer auth token required to make API calls.
    '''
    EXPIRES_IN = "expiresIn"
    BUFFER_TIME = 5*60 # 5 mins

    def __init__(self, token=None, token_acquired_at=None):
        self.token = token
        self.token_acquired_at = token_acquired_at
        

    def has_token_expired(self): 
        if self.token is None:
            return True
        expires_in = self.token[AuthenticationHelper.EXPIRES_IN] 
        token_time_elapsed = int((datetime.utcnow() - self.token_acquired_at).total_seconds())
        LOG.info("Token in use for {} seconds, expires_in {} seconds".format(
                 token_time_elapsed,
                 expires_in - AuthenticationHelper.BUFFER_TIME))
        return (token_time_elapsed >= 
                expires_in - AuthenticationHelper.BUFFER_TIME)


    def get_access_token(self):
        '''
        Generates the access token and returns it.
        :rtype: dict
        '''
        NotImplementedError("This is meant to be implemented by derived classes.")
