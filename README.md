# noaa_docker

This repo holds the partner docker code for NOAA. This allows AzureFarmbeats customers to get NOAA weather data in their farmbeats' installations.

## How to use this sample and build your own docker

If you're a partner. If you look in the partners folder, you'll find three directories. These are the three things you need to think about. 
1. Bootstrap
2. Jobs
3. Deployment
Let's look at each one.

### 1. Bootstrap
In this phase you're thinking what jobs will you run, their structure and the data that they will bring in. 
If you look in the bootstrap folder, it contains the bootstrap_manifest.json, this is the only thing you need to concern yourself with. There is another file bootstrap.py, this takes the manifest and orchestrates the bootstrap. It maybe instructive to take a look at it, in particular the **run** function. This gives you an idea of the **workflow**.

def run(config_file, end_point, function_url):
    
    # create the bootstrap object - that will bootstrap the partner
    LOG.info("Creating bootstrap object")
    bootstrap = Bootstrap(config_file=config_file, end_point=end_point, function_url=function_url)
    LOG.info("Successfully created bootstrap object")

    # add new extended measure types
    LOG.info("Adding the new measure types")
    bootstrap.add_new_extended_measure_types()
    LOG.info("Successfully added the new measure types")

    # add new measure units
    LOG.info("Adding the new measure units")
    bootstrap.add_new_extended_measure_units()
    LOG.info("Successfully added the new measure units") 

    # upsert the weather data models
    LOG.info("Upserting new weather data models")
    bootstrap.upsert_weather_data_models()
    LOG.info("Successfully upserted the weather data models")

    # upsert the job types
    LOG.info("Upserting the job types")
    bootstrap.upsert_job_types()
    LOG.info("Successfully upserted the job types")

Now, if you open the bootstrap_manifest.json. You'll find 4 elements
* add_extended_measure_types
* add_extended_measure_units
* add_data_models
* add_job_types

The way to think about extended types, is having an API exposed to CRUD enums into the system. It allows some level of type checking while ingesting data. Data with only defined types can be entered in the system. This goes a long way in preventing accidental typos, other inaccuracies etc. to enter the system.

#### add_extended_measure_types
This is where you look at what's already defined and what else you need. Once, you have finalized on the data that you need, you need to figure out which **measures** do not exist in the system. Here the sample is for weather partner NOAA. These are the missing measures under ExtendedTypes>key=WeatherMeasureType
```
 "add_extended_measure_types":[
        "Elevation",
        "WindAngle",
        "SeaLvlPressure",
        "PresentWeatherIndicator",
        "PastWeatherIndicator",
        "PrecipTime",
        "PrecipDepth",
        "SnowDepth"
    ]
```

#### add_extended_measure_units
Similar to the measures, you need to ensure that the required **units** for these measures exist in the system. Here the sample is for weather parther NOAA. These are the missing units under ExtendedTypes>key=WeatherMeasureUnit
```
  "add_extended_measure_units":[
        "Hectopascals",
        "Hours"
    ]
```

#### add_data_models
This is where you add the required (one or more) data models to the system. Since, this is an example for a weather partner (NOAA). What's added is a list of WeatherStationModels. Each weather station model as expected holds a list of weatherStationMeasures. This is the schema for your data. 

```
"add_data_models":[
        {
            "name": "noaa_isd",
            "description": "NOAA integrated surface database - weather data",
            "weatherStationMeasures": [
              {
                "name": "elevation",
                "dataType": "Double",
                "type": "Elevation",
                "unit": "NoUnit",
                "description": "The elevation of a GEOPHYSICAL-POINT-OBSERVATION relative to Mean Sea Level (MSL)."
              },
              {
                "name": "windAngle",
                "dataType": "Double",
                "type": "WindAngle",
                "unit": "Degree",
                "description": "The angle, measured in a clockwise direction, between true north and the direction from which the wind is blowing. MIN: 001 MAX: 360 UNITS: Angular Degrees"
              },
              {
                "name": "temperature",
                "dataType": "Double",
                "type": "AmbientTemperature",
                "unit": "Celsius",
                "description": "The temperature of the air. MIN: -0932 MAX: +0618 UNITS: Degrees Celsius"
              },
              {
                "name": "seaLvlPressure",
                "dataType": "Double",
                "type": "SeaLvlPressure",
                "unit": "Hectopascals",
                "description": "The air pressure relative to Mean Sea Level (MSL). MIN: 08600 MAX: 10900 UNITS: Hectopascals"
              },
              {
                "name": "precipTime",
                "dataType": "Double",
                "type": "PrecipTime",
                "unit": "Hours",
                "description": "The quantity of time over which the LIQUID-PRECIPITATION was measured. Units: Hours. MIN: 00; MAX: 98; 99 = Missing."
              },
              {
                "name": "precipDepth",
                "dataType": "Double",
                "type": "PrecipDepth",
                "unit": "MilliMeter",
                "description": "The depth of LIQUID-PRECIPITATION that is measured at the time of an observation. Units: millimeters. MIN: 0000; MAX: 9998; 9999 = Missing."
              },
              {
                "name": "snowDepth",
                "dataType": "Double",
                "type": "SnowDepth",
                "unit": "CentiMeter",
                "description": "The depth of snow and ice on the ground. MIN: 0000 MAX: 1200 UNITS: centimeters"
              }
            ],
            "properties": {
            }
          }
    ]
```

#### add_job_types
Finally, you add your **job** definition(s) as job types. For example, you want to add a get_weather_data job, which gets weather data for a given location (lat, long) for a given date range. All of these you will see in the pipeline parameters. In the background, this creates a [Azure Data Factory](https://azure.microsoft.com/en-in/resources/videos/azure-data-factory-overview/) pipeline with the provided parameters. You don't need to worry about the other pipeline details like resourceGroupName, dataFactoryName, pipelineName. Since the pipeline will be created for you when you set the boolean isPartnerJobType to true, these values will be overwritten once the pipeline is provisioned.
```
"add_job_types":[
        {
            "name": "get_weather_data",
            "description": "Get weather data (NOAA ISD) - Azure open datasets",
            "isPartnerJobType": true,
            "pipelineDetails": {
              "parameters": [
                {
                  "name": "latitude",
                  "type": "Float",
                  "isRequired": true,
                  "description": "Latitude for the point for which we want to fetch weather data"
                },
                {
                    "name": "longitude",
                    "type": "Float",
                    "isRequired": true,
                    "description": "Longitude for the point for which we want to fetch weather data"
                },
                {
                    "name": "start_date",
                    "type": "String",
                    "isRequired": true,
                    "description": "Date from which (inclusive) weather data will be downloaded for the farm. Format is YYYY-MM-DD. Example: 2019-09-28"
                },
                {
                    "name": "end_date",
                    "type": "String",
                    "isRequired": true,
                    "description": "Date to which (inclusive) weather data will be downloaded for the farm. Format is YYYY-MM-DD. Example: 2019-09-28"
                },
                {
                    "name": "farm_id",
                    "type": "String",
                    "isRequired": false,
                    "description": "System generated unique Farm Id. Please refer to Farm APIs for more information."
                }
              ]
            },
            "properties":{
              "programRunCommand": "python3 noaa/jobs/get_weather_data.py"
            }
        }
     ]
```

### 2. Jobs
In the jobs folder, you'll see the actual job code. Again, it may be instructive to look at the **workflow**. For, instance take **get_weather_data** function.

```
     def __get_weather_data_for_day(self, day, lat, lon):
        '''
        Gets weather data for a given day and pushes it to eventhub
        '''
        try:
            # get data for given date range.
            start_time = time.time()
            LOG.info("Getting data for " + day.strftime("%m/%d/%Y, %H:%M:%S"))
            weather_data = NoaaIsdWeather(day, day)
            LOG.info("Successfully got data for " + day.strftime("%m/%d/%Y, %H:%M:%S"))

            # get the data into a pandas data frame, so we can filter and process
            weather_data_df = weather_data.to_pandas_dataframe()
            LOG.info("Took {} seconds to get the data.".format(time.time() - start_time))

            # out of the lat longs available get the nearest points
            LOG.info("Finding the nearest latitude and longitude from the available data")
            (nearest_lat, nearest_lon) = UtilFunctions.find_nearest_lat_longs_in_data(weather_data_df, lat, lon)
            LOG.info("nearest lat, lon: [" + str(nearest_lat) + "," + str(nearest_lon) + "]")

            # filter the data to this lat and lon
            LOG.info("Filtering the data to nearest lat, lon")
            filtered_weather_data = weather_data_df[(weather_data_df['latitude'] == nearest_lat) & (weather_data_df['longitude'] == nearest_lon)]
            LOG.info(filtered_weather_data)

            # push the data to eventhub
            LOG.info("Pushing data to eventhub")
            wdl_id = self.__push_weather_data_to_farmbeats(filtered_weather_data)
            LOG.info("Successfully pushed data")

            # Update the status for the job
            if FLAGS.job_status_blob_sas_url:
                msg = "Weather data pushed for start_date: {} to end_date: {}\n for nearest_lat: {}, nearest_lon: {}\n provided lat:{}, lon:{}".format(
                    FLAGS.start_date, FLAGS.end_date, nearest_lat, nearest_lon, FLAGS.latitude, FLAGS.longitude)
                writer = JobStatusWriter(FLAGS.job_status_blob_sas_url)
                output_writer = writer.get_output_writer()
                output_writer.set_prop("WeatherDataLocationId: ", wdl_id)
                output_writer.set_prop("Message: ", msg)
                writer.set_success(True)
                writer.flush()

        except Exception as err:
            ...

```
This is where you write the code that will pull data from your source and push it to farmbeats. In case of NOAA, we are pulling the data from [Azure open datasets - NOAA ISD](https://azure.microsoft.com/en-in/services/open-datasets/catalog/noaa-integrated-surface-data/). Doing the processing required; we need to filter out the data based on provided location of interest (latitude, longitude) and then pushing this data to an [EventHub](https://docs.microsoft.com/en-us/azure/event-hubs/) in farmbeats.

## 2.1 Authentication
There are three points of communication
1. Pulling data from your own source for which you have partner credentials.
2. Calling datahub APIs for creating WeatherDataLocation, querying WeatherDataModelId etc. 
3. Pushing data to eventhub

Access to all of them is provided using ExtendedPropertiesReader class in datahub_lib. An example can be found in constructors of GetWeatherDataJob or GetWeatherForecastDataJob.  

### 3. Deployment
Finally comes deployment. Now, you have updated the bootstrap_manifest and implemented your jobs. You need to make the whole thing available to customers. This you do by containerizing the code. To that end, you have to implement your own docker file [documentation](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/), this will enable you to build the docker image, which you can upload to a docker container registry of your choice. Ofcourse, we recommend you do so in dockerhub. Feel free to look at the dockerfile provided for the sample. It's build on top of an ubuntu base image, installs python, the required dependencies and copies the code.
