'''
This module contains constants related to scene.
'''
ENVIRONMENT_VARIABLE_LOG_LEVEL = "LOG_LEVEL"

class SceneConstants:
    '''
    Constants required to understand/parse the
    Geospatial scene (i.e., the metadata and geotif files).
    '''
    NODATA_VALUE = -9999
    UINT_NODATA_VALUE = 65535
    DARK_PIX_VALUE = 0

    NO_CLOUD_VALUE = 0
    OPAQUE_CLOUD_VALUE = 1
    CIRRUS_CLOUD_VALUE = 2
    OTHER_CLOUD_VALUE = 3

    CLOUD_MASK_KEY = 'CLOUD_MASK'
    CLOUD_MASK_METADATA = '0:CLEAR,1:OPAQUE,2:CIRRUS'

    # These are keys in scene's metadata
    CLOUD_COVER_PERC = "CloudCoverPercentage"
    DARK_PIXEL_PERC = "DarkPixelPercentage"
    BOUNDINGRECT_KEY = "BoundingRect" # bounding rect of farm area
    FARM_EXTENT_KEY = "FarmExtent"   # actual farm geojson

    # sentinel original metadata keys
    ORG_CLOUD_COVER_KEY = "Cloud cover percentage"
        