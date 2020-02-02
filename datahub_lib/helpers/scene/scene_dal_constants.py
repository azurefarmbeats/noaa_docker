'''
This module contains constants related to scene API.
These constants are defined by API (majorly), used while
reading and writing scenes and scenefiles to API store.
SceneConstants are different from SceneDALConstants.
SceneConstants are related to GeospatialScene objects
having different naming convention.
'''

class SceneAPIConstants:
    SCENE_ROUTE = "/Scene"
    SCENE_FILE_ROUTE = "/SceneFile"


class SceneDALConstants:
    ID = "id"
    TYPE = "type"
    SOURCE = "source"
    FARM_ID = "farm_id"
    FARM_ID_INSERT = "farmId"
    JOB_ID = "jobId"
    NAME = "name"
    DATE = "_date"
    DATE_INSERT = "date"
    SEQUENCE = "sequence"
    DESCRIPTION = "description"
    PROPERTIES = "properties"
    CLOUD_COVER_PERCENTAGE = "CloudCoverPercentage"
    DARK_PIXEL_PERCENTAGE = "DarkPixelPercentage"
    NDVI_MEDIAN_VALUE = "NDVIMedianValue"
    FARM_EXTENT = "FarmExtent"

    # for authorization
    RESOURCE = "resource"
    CLIENT_ID = "client_id"
    THUMBPRINT = "thumbprint"
    TENANT_ID = "tenant_id"
    PASSWORD_FILE = "password_file"
    BEARER = "Bearer"
    AUTHORIZATION = "authorization"
    ACCESS_TOKEN = "accessToken"

    # Query Params
    TYPES = "types"
    SOURCES = "sources"
    MIN_SCENE_DATE = "minSceneDate"
    MAX_SCENE_DATE = "maxSceneDate"
    ITEMS = "items"


class SceneFileDALConstants:
    ID = "id"
    CONTENT_TYPE = "content_type"
    CONTENT_TYPE_INSERT = "contentType"
    TYPE = "type"
    NAME = "name"
    SCENE_ID_INSERT = "sceneId"
    DESCRIPTION = "description"
    PROPERTIES = "properties"
    BLOB_URL = "blob_url"
    DOWNLOAD_SAS_URL = "download_sas_url"
    UPLOAD_SAS_URL = "upload_sas_url"
    RESOLUTION = "resolution"
    WAVELENGTH = "wavelength"

    # Query Params
    TYPES = "types"
    ITEMS = "items"
    CONTENT_TYPES = "contentTypes"
