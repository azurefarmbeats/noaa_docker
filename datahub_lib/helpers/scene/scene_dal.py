'''
Wrapper class to access Scene data from store using Scene API.
'''
# System imports
import os
import json
from datetime import datetime, date, timedelta

# Local imports
from datahub_lib.framework.logger import Logger
from datahub_lib.helpers.utils.date import DateTimeUtil
from datahub_lib.helpers.scene.scene_dao import SceneDAO
from datahub_lib.helpers.scene.scene_dal_constants import SceneDALConstants, SceneFileDALConstants
from datahub_lib.helpers.scene.scene_dal_constants import SceneAPIConstants
from datahub_lib.helpers.scene.scene_file_dao import SceneFileDAO
from datahub_lib.framework.fb_api import FarmbeatsApi
from datahub_lib.helpers.utils.blob_util import BlobUtil

LOG = Logger.get_logger()

class SceneDAL:
    '''
    Class to get and post scene data from/to store using Scene API.
    '''
    def __init__(self, farmbeats_api: FarmbeatsApi):
        self.farmbeats_api = farmbeats_api


    def delete_scene(self, scene_id:str):
        '''
        Deletes scene from store using API for given scene_id.
        '''
        self.__delete_scene_files(scene_id)
        self.farmbeats_api.get_scene_api().scene_delete_scene(id=scene_id)


    #TODO: take scene_type and source as list
    def get_scenes(self, farm_id: str, from_date: date, to_date: date,
                   scene_type: str=None, source: str=None) -> list:
        '''
        Get scenes from store using API for given farmid and filters.
        :param str farm_id: unique id representing farm
        :param date from_date: start date to filter scenes
        :param date to-date: end date to filter scenes
        :param str scene_type: type of scene, optional
        :param str source: source of scene, optional
        :return: returns list of SceneDAO objects.
        :rtype: list
        '''
        LOG.info('Querying store using API to get scenes')
        params = {}
        if from_date:
            params[SceneDALConstants.MIN_SCENE_DATE] \
                = DateTimeUtil.to_datetime(from_date).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        if to_date:
            to_date_updated = to_date + timedelta(hours=24)
            params[SceneDALConstants.MAX_SCENE_DATE] \
                = DateTimeUtil.to_datetime(to_date_updated).strftime('%Y-%m-%dT%H:%M:%S.%fZ')


        scenes_json_list = self.farmbeats_api.get_scene_api().scene_get_all_scenes(
            farm_id = farm_id, 
            min_scene_date = params[SceneDALConstants.MIN_SCENE_DATE] if from_date else None,
            max_scene_date = params[SceneDALConstants.MAX_SCENE_DATE] if to_date else None, 
            types = [scene_type] if type else None,
            sources = [source] if source else None
        ).to_dict().get(SceneDALConstants.ITEMS)

        LOG.info("Got %d scenes from store" % len(scenes_json_list))

        scenes_list = []
        for scene_json in scenes_json_list:
            scenes_list.append(SceneDAO.from_dict(scene_json))

        return scenes_list


    def get_scene_file_ids(self, scene_id: str) -> list:
        '''
        Get scene file ids from store using API given scene_id.
        :param str scene_id: unique id representing farm scene
        :return: returns list of scene file ids.
        :rtype: list
        '''
        response_files = self.farmbeats_api.get_scene_file_api().scene_file_get_all_scenes_files(
            scene_id = scene_id).to_dict().get(SceneDALConstants.ITEMS)

        scene_file_ids = []
        if response_files is not None: 
            for response in response_files:
                scene_file_ids.append(response[SceneDALConstants.ID])

        return scene_file_ids


    def get_scene_files(self, scene_id: str, sceneFileType: str, target_dir: str,
                        content_types: list=None, filters:dict={}) -> list:
        '''
        Get scene file from store using API given scene_id, type and other filters.
        :param str scene_id: unique id representing farm
        :param str scene_file_type: type of scene file
        :param str target_dir: dir path to download files
        :param list content_types: list of file content types to filter, optional
        :param dict filters: key value pairs of scene file properties to filter, optional
        :return: returns list of SceneFileDAO objects.
        :rtype: list
        '''
        response_files = self.farmbeats_api.get_scene_file_api().scene_file_get_all_scenes_files(
            scene_id = scene_id, generate_download_sas_url = True, types = [sceneFileType],
            content_types = content_types if content_types else None
        ).to_dict().get(SceneFileDALConstants.ITEMS)

        scene_files_list = []
        for response in response_files:
            properties = response[SceneDALConstants.PROPERTIES]
            if not filters or (filters and self.__validate_filters(filters, properties)):
                sas_url = response[SceneFileDALConstants.DOWNLOAD_SAS_URL]
                scene_file_dao = SceneFileDAO.from_dict(response)
                scene_file_dao.local_path, _ = BlobUtil.download_using_sas_url(sas_url, target_dir)
                scene_files_list.append(scene_file_dao)

        return scene_files_list


    def insert_scene(self, obj: SceneDAO):
        '''
        Inserts given SceneDAO object into store using SceneAPI,
        :param SceneDAO obj: object to insert to store
        :return: returns sceneid of inserted scene.
        :rtype: str
        '''
        LOG.info('Inserting scene to store using Scene API')
        scene_id = None
        response = self.farmbeats_api.get_scene_api().scene_create(input=obj.to_dict())

        if not response:
            raise Exception("Error inserting scene to store")
        else:
            scene_id = response.to_dict().get(SceneDALConstants.ID)

        return scene_id


    def insert_scene_files(self, scene_id: str, scene_files: list):
        '''
        Insert all the scene files to store.
        :param str scene_id: unique id representing scene in store.
        :param list scene_files: list of SceneFileDAO objects
        '''
        # create the input list
        for file in scene_files:
            file.scene_id = scene_id
            response = self.farmbeats_api.get_scene_file_api().scene_file_create_scene_file(input=file.to_dict())
            sas_url = response.to_dict().get(SceneFileDALConstants.UPLOAD_SAS_URL)
            BlobUtil.upload_using_sas_url(sas_url, file.local_path)


    def __delete_scene_files(self, scene_id:str):
        '''
        Deletes scene files from store using API for given scene_id.
        '''
        scene_file_ids = self.get_scene_file_ids(scene_id)
        for scene_file_id in scene_file_ids:
            LOG.info("Deleting scene file %s of scene %s", scene_file_id, scene_id)
            self.farmbeats_api.get_scene_file_api().scene_file_delete_scene_file(id=scene_file_id)
    

    def __validate_filters(self, query_filters: dict, properties: dict) -> bool:
        '''
        Returns if query filters is subset of properties.
         '''
        for key,value in query_filters.items():
             if((key, value) not in properties.items()):
                return False

        return True
