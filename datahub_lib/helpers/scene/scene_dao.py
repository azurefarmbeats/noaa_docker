'''
Class representing Scene from Scene API.
'''
# System imports
import json
from datetime import date, datetime

# Local imports
from datahub_lib.framework.logger import Logger
from datahub_lib.helpers.utils.date import DateTimeUtil
from datahub_lib.framework.logger import Logger
from datahub_lib.helpers.scene.scene_dal_constants import SceneDALConstants

LOG = Logger.get_logger()


class SceneDAO:
    '''
    Class representing Scene object from Scene API.
    '''

    def __init__(self, type: str, source: str, farm_id: str, date: date,
                 scene_id: str=None, job_id: str=None, name: str='default name',
                 sequence: int=0, description: str='No description', properties: dict={}):
        # required fields for scene api model
        self.type = type
        self.source = source
        self.farm_id = farm_id
        self.date = date # represents scene date
        self.name = name

        # optional fields
        self.scene_id = scene_id
        self.job_id = job_id
        self.sequence = sequence
        self.description = description
        self.properties = properties


    def to_dict(self) -> dict:
        '''
        Converts this object to dict.
        :return: returns dictionary representing this object.
        :rtype: dict
        '''
        ret = {}

        # Scene type cannot have '.' character in them - make sure they follow
        ret[SceneDALConstants.TYPE] = self.type.replace('.','')
        ret[SceneDALConstants.SOURCE] = self.source
        ret[SceneDALConstants.FARM_ID_INSERT] = self.farm_id
        ret[SceneDALConstants.JOB_ID] = self.job_id
        ret[SceneDALConstants.SEQUENCE] = self.sequence

        # datetime outputs microseconds, we need milliseconds.
        ret[SceneDALConstants.DATE_INSERT] = datetime(
            self.date.year,
            self.date.month,
            self.date.day).strftime(format='%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        ret[SceneDALConstants.NAME] = self.name
        ret[SceneDALConstants.DESCRIPTION] = self.description
        ret[SceneDALConstants.PROPERTIES] = self.properties
        return ret


    @staticmethod
    def from_dict(scene: dict):
        '''
        Returns SceneDAO object give dictionary.
        '''
        return SceneDAO(type=scene[SceneDALConstants.TYPE],
                       source=scene[SceneDALConstants.SOURCE],
                       farm_id=scene[SceneDALConstants.FARM_ID],
                       date=DateTimeUtil.to_datetime(scene[SceneDALConstants.DATE]).date(),
                       scene_id=scene[SceneDALConstants.ID],
                       name=scene[SceneDALConstants.NAME],
                       sequence=int(scene[SceneDALConstants.SEQUENCE]),
                       description=scene[SceneDALConstants.DESCRIPTION],
                       properties=scene[SceneDALConstants.PROPERTIES])
