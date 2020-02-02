'''
Test token caching
'''
# System imports 
from datetime import datetime
import time

# 3rd party imports
import pytest

# Local imports
from datahub_lib.auth.fb_auth_helper import FarmbeatsAuthHelper

@pytest.mark.parametrize('token, has_expired', 
 [
    (None, True),
    ({
    'tokenType': 'Bearer',
    'expiresIn': 3599,
    'resource': 'https://fbinstant-datahub.azurewebsites.net',
    'accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImllX3FXQ1hoWHh0MXpJRXN1',
    'isMRRT': True,
    '_clientId': '4dbb9bd4-d65a-4ff9-bacd-c7e31264f30c',
    '_authority': 'https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47'
    }, False),
    ({
    'tokenType': 'Bearer',
    'expiresIn': 1,
    'resource': 'https://fbinstant-datahub.azurewebsites.net',
    'accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImllX3FXQ1hoWHh0MXpJRXN1',
    'isMRRT': True,
    '_clientId': '4dbb9bd4-d65a-4ff9-bacd-c7e31264f30c',
    '_authority': 'https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47'
    }, True)
 ])
def test_token_cache(token, has_expired):
    # TODO: Once we decide the test-environment and check-in the test config,
    # change this init. Also, get real valid tokens instead of hardcoding. 
    auth_helper = FarmbeatsAuthHelper(api_endpoint=None,
                                       tenant_id=None,
                                       app_id = None,
                                       app_client_secret= None)
    auth_helper.token = token                                
    auth_helper.token_acquired_at = datetime.utcnow()
    time.sleep(2)
    assert auth_helper.has_token_expired() == has_expired
