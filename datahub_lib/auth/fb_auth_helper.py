'''
This module generates bearer auth token required to make API calls.
'''

# system imports
import os
import adal
import time
from datetime import datetime 

# 3rd party imports
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_active_directory import AADTokenCredentials

# local imports
from datahub_lib.framework.logger import Logger
from datahub_lib.auth.authentication_helper import AuthenticationHelper
LOG = Logger.get_logger()


class FarmbeatsAuthHelper(AuthenticationHelper):
    '''
    Class to get and manage the access token to farmbeats. 
    It gets the access token using AAD app client ID and secret. 
    '''
    AUTHORITY_HOST_URL = "https://login.microsoftonline.com/"
    RESOURCE_HOST_URL = "https://management.core.windows.net/"

    def __init__(self, api_endpoint: str, tenant_id: str, app_id: str, app_client_secret: str):
        AuthenticationHelper.__init__(self)
        self.api_endpoint = api_endpoint
        self.tenant_id = tenant_id
        self.app_id = app_id
        self.app_client_secret = app_client_secret


    def get_access_token(self):
        '''
        Generates the access token and returns it.
        :rtype: dict
        '''
        if self.has_token_expired():
            context = adal.AuthenticationContext(
                FarmbeatsAuthHelper.AUTHORITY_HOST_URL + self.tenant_id)
            self.token = context.acquire_token_with_client_credentials(self.api_endpoint,
                    self.app_id, self.app_client_secret)
            self.token_acquired_at = datetime.utcnow()
        return self.token


    def authenticate_client_cert(self) -> ServicePrincipalCredentials:
        """
        Authenticate using service principal w/ cert.
        """
        authority_uri = FarmbeatsAuthHelper.AUTHORITY_HOST_URL + self.tenant_id
        context = adal.AuthenticationContext(
            authority_uri,
            api_version=None)

        mgmt_token = context.acquire_token_with_client_credentials(
            FarmbeatsAuthHelper.RESOURCE_HOST_URL,
            self.app_id,self.app_client_secret)

        credentials = AADTokenCredentials(mgmt_token, self.app_id)
        return credentials
