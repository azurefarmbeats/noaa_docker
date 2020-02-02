'''
Class representing Scene File from Scene API.
'''

from datahub_lib.helpers.scene.scene_dal_constants import SceneFileDALConstants

class SceneFileDAO:
    '''
    Class representing SceneFile object from Scene API.
    '''

    def __init__(self, content_type: str, type: str, scene_id: str=None,
                 name: str=None, description: str='No description',
                 local_path: str=None, remote_url: str=None,
                 download_sas_url: str=None, properties: dict={}):

        # required fields for scene api model
        self.content_type = content_type
        self.type = type
        self.scene_id = scene_id   # Optional for ctor but assign scene_id before post api call
        self.name = name

        # optional fields
        self.description = description
        self.properties = properties

        self.local_path = local_path
        self.remote_url = remote_url
        self.download_sas_url = download_sas_url


    def to_dict(self) -> dict:
        '''
        Converts this object to dict.
        :return: returns dictionary representing this object.
        :rtype: dict
        '''
        ret = {}
        ret[SceneFileDALConstants.CONTENT_TYPE_INSERT] = self.content_type
        ret[SceneFileDALConstants.SCENE_ID_INSERT] = self.scene_id
        ret[SceneFileDALConstants.TYPE] = self.type
        ret[SceneFileDALConstants.NAME] = self.name
        ret[SceneFileDALConstants.DESCRIPTION] = self.description
        ret[SceneFileDALConstants.PROPERTIES] = self.properties
        return ret


    @staticmethod
    def from_dict(scene_file: dict):
        '''
        returns SceneFileDAO object given dict.
        '''
        return SceneFileDAO(
            content_type=scene_file[SceneFileDALConstants.CONTENT_TYPE],
            type=scene_file[SceneFileDALConstants.TYPE],
            name=scene_file[SceneFileDALConstants.NAME],
            description=scene_file[SceneFileDALConstants.DESCRIPTION],
            remote_url=scene_file[SceneFileDALConstants.BLOB_URL],
            properties=scene_file[SceneFileDALConstants.PROPERTIES])
