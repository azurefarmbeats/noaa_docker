# system imports
import os

# 3rd party imports
from azure.storage.blob import BlockBlobService
from urllib.parse import urlparse

# Local imports
from datahub_lib.framework.logger import Logger

LOG = Logger.get_logger()

class BlobUtil:
    '''Helper class to upload/download to/from a blob using SAS url'''


    def __init__(self):
        pass


    @staticmethod
    def upload_using_sas_url(sas_url :str, file_full_path :str, etag :str = None):
        """
        Method to upload file to Azure blob container using SAS url.
        :param sas_url: SAS url with write access to blob storage
        :param file_full_path: Full path of file to be uploaded.
        """
        sas_info = urlparse(sas_url)
        container_name, blob_name = BlobUtil.parse_blob_path(sas_info.path)
        storage_account_name = sas_info.netloc.split(".")[0]

        blob_service = BlockBlobService(
            account_name=storage_account_name,
            sas_token=sas_info.query)

        # Tried with '*' as default value for etag, as specified in the documentation.
        # It worked in local but failed in cloud (pipeline).
        # None as default value works both in local and in cloud (pipeline) but not
        # mentioned as the way to go in the documentation. 
        # So, this if block is just so that existing code path stays unaffected. 
        response = None
        if etag is None: 
            response = blob_service.create_blob_from_path(
                        container_name=container_name,
                        blob_name=blob_name,
                        file_path=file_full_path)
        else:
            response = blob_service.create_blob_from_path(
                        container_name=container_name,
                        blob_name=blob_name,
                        file_path=file_full_path,
                        if_match=etag)
        LOG.info("Successfully uploaded file to %s", blob_name)
        return response
        

    @staticmethod
    def download_using_sas_url(sas_url: str, target_dir: str):
        """
        Method to download file to target directory using SAS url.
        :param str sas_url: SAS url with read access to blob storage
        :param str target_dir: directory where file will be downloaded to.
        :return: returns downloaded file path
        :rtype: str
        """
        sas_info = urlparse(sas_url)
        container_name, blob_name = BlobUtil.parse_blob_path(sas_info.path)
        storage_account_name = sas_info.netloc.split(".")[0]

        blob_service = BlockBlobService(
            account_name=storage_account_name,
            sas_token=sas_info.query)

        file_name = os.path.basename(blob_name)
        target_path = os.path.join(target_dir,file_name)
        
        response = blob_service.get_blob_to_path(
                    container_name=container_name,
                    blob_name=blob_name,
                    file_path=target_path)
        etag = response.properties.etag
        LOG.info("Successfully downloaded file to %s", target_path)
        return (target_path, etag)


    @staticmethod
    def parse_blob_path(blob_path: str):
        '''
        Parse blob url and returns container_name and blob path.
        :param str blob_path: blob path without storage account details at start.
        :return: returns tuple of container and blob names.
        :rtype: tuple
        '''
        if blob_path[0] == '/':
            blob_storage_path = blob_path[1:]
        else:
            blob_storage_path = blob_path

        split_values = str(blob_storage_path).split("/")
        container_name = split_values[0]
        blob_name = "/".join(split_values[1:])
        return [container_name, blob_name]
