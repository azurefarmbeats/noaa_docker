class JobConstants:
    # Error codes
    INTERNAL_ERROR = '500'
    BAD_REQUEST = '400'

    # TELEMETRY
    WEATHER_TELEMETRY_FORMAT = '''{
                                    "weatherdatalocations": [
                                        {
                                        "id": "",
                                        "weatherdata": []
                                        }
                                    ]
                                }'''

    # API 
    WEATHER_DATA_LOCATIONS = "weatherdatalocations"
    WEATHER_DATA = "weatherdata"
    ID = "id"
    ITEMS = "items"
    WEATHER_MEASURES = "WeatherMeasures"
    PROPERTIES = "Properties"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    LOCATION = "location"
    WEATHER_DATA_MODEL_ID = "weather_data_model_id"
    WEATHER_DATA_MODEL_ID_PAYLOAD = "weatherDataModelId"
    NAME = "name"
    FARM_ID = "farmid"
