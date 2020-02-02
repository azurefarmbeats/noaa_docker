# System imports
import json

# Local imports 
from datahub_lib.framework.fb_api import FarmbeatsApi

class FarmUtil:
    '''
    provides utility functions for the farm
    '''
    
    EXTENT = "geometry"

    def __init__(self, farmbeats_api: FarmbeatsApi):
        self.farmbeats_api = farmbeats_api


    def get_farm_extent(self, farm_id: str):
        '''
        returns the farm extent, given the farm id.
        param: str: farm_id
        rparam: str
        '''
        farm_extent = self.farmbeats_api.get_farm_api().farm_get(id=farm_id).to_dict()[FarmUtil.EXTENT]
        return json.dumps(farm_extent)
