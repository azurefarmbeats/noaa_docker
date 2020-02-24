# coding: utf-8

# flake8: noqa
"""
    Azure FarmBeats API

    <p>  <p>Azure FarmBeats helps you build digital agricultural solutions in Azure. By providing a standardized schema to query agricultural data from various sources, Azure FarmBeats provides you:  <ul >   <li style=\"margin: 7px;\">Ability to acquire, aggregate, process and store agricultural data.</li>   <li style=\"margin: 7px;\">Capability to fuse data between data sources and generate insights.</li>   <li style=\"margin: 7px;\">Schematized access and query capabilities on ingested data.</li>  </ul>  </p>  <h><b>REST Operation Groups</b></h>  <p><b>Farm:</b></p>  <p>Farm corresponds to a physical location of interest within the system. Each Farm has a Farm name and a unique farm id.</p>  <p><b>Device:</b></p>  <p>Device corresponds to a physical device present in the farm. Each device has a unique device id. Device is typically provisioned to a farm with a farm id.</p>  <p><b>DeviceModel:</b></p>  <p>DeviceModel corresponds to the meta-data of the device such as the Manufacturer, Type of the device either Gateway or Node.</p>  <p><b>Sensor:</b></p>  <p>Sensor corresponds to a physical sensor that records values. A sensor is typically connected to a device with a device id.</p>  </p>  <p><b>SensorModel:</b></p>  <p>SensorModel corresponds to the meta-data of the sensor such as the Manufacturer, Type of the sensor either Analog or Digital, Sensor Measure such as Ambient Temperature, Pressure etc.</p>  <p><b>Telemetry:</b></p>  <p>Telemetry provides the ability to read telemetry messages for a particular sensor & time range.</p>  <p><b>Job:</b></p>  <p>Job corresponds to any workflow of activities which are executed in the system to get a desired output. Each job is associated with a job id and job type.</p>  <p><b>JobType:</b></p>  <p>JobType corresponds to different job types supported by the system. This includes system defined & user-defined job types.</p>  <p><b>ExtendedType:</b></p>  <p>ExtendedType corresponds to the list of system & user-defined types in the system. This helps setup a new Sensor or Scene or Scenefile type in the system.</p>  <p><b>Partner:</b></p>  <p>Partner corresponds to the sensor/weather/imagery integration partner.</p>  <p><b>Scene:</b></p>  <p>Scene corresponds to any generated output in the context of a Farm. Each Scene has a scene id, scene source, scene type and farm id associated with it. Each scene id  can have multiple scene files associated with it.</p>  <p><b>SceneFile:</b></p>  <p>SceneFile corresponds to all files which are generated for single scene. A single scene id can have multiple SceneFile ids associated with it.</p>  <p><b>Rule:</b></p>  <p>Rule corresponds to a condition for farm-related data to trigger an alert. Each rule will be in the context of a farm's data.</p>  <p><b>Alert:</b></p>  <p>Alert corresponds to a notification which gets generated when a rule condition is met. Each alert will be in the context of a rule.</p>  <p><b>RoleDefinition:</b></p>  <p>RoleDefinition defines allowed and disallowed actions for a role.</p>  <p><b>RoleAssignment:</b></p>  <p>RoleAssignment corresponds to the assignment of a role to a user or a service principal.</p>  </p>    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from datahub_lib.swagger_client.models.alert_request import AlertRequest
from datahub_lib.swagger_client.models.alert_response import AlertResponse
from datahub_lib.swagger_client.models.alert_response_list_response import AlertResponseListResponse
from datahub_lib.swagger_client.models.azure_batch_details import AzureBatchDetails
from datahub_lib.swagger_client.models.condition import Condition
from datahub_lib.swagger_client.models.create_scene_file_response import CreateSceneFileResponse
from datahub_lib.swagger_client.models.credentials import Credentials
from datahub_lib.swagger_client.models.date_time_range import DateTimeRange
from datahub_lib.swagger_client.models.debug_information import DebugInformation
from datahub_lib.swagger_client.models.device_model_request import DeviceModelRequest
from datahub_lib.swagger_client.models.device_model_response import DeviceModelResponse
from datahub_lib.swagger_client.models.device_model_response_list_response import DeviceModelResponseListResponse
from datahub_lib.swagger_client.models.device_port import DevicePort
from datahub_lib.swagger_client.models.device_request import DeviceRequest
from datahub_lib.swagger_client.models.device_response import DeviceResponse
from datahub_lib.swagger_client.models.device_response_list_response import DeviceResponseListResponse
from datahub_lib.swagger_client.models.docker_details import DockerDetails
from datahub_lib.swagger_client.models.extended_type_request import ExtendedTypeRequest
from datahub_lib.swagger_client.models.extended_type_response import ExtendedTypeResponse
from datahub_lib.swagger_client.models.extended_type_response_list_response import ExtendedTypeResponseListResponse
from datahub_lib.swagger_client.models.farm_request import FarmRequest
from datahub_lib.swagger_client.models.farm_response import FarmResponse
from datahub_lib.swagger_client.models.farm_response_list_response import FarmResponseListResponse
from datahub_lib.swagger_client.models.get_scene_file_response import GetSceneFileResponse
from datahub_lib.swagger_client.models.get_scene_file_response_list_response import GetSceneFileResponseListResponse
from datahub_lib.swagger_client.models.i_action import IAction
from datahub_lib.swagger_client.models.icrs_object import ICRSObject
from datahub_lib.swagger_client.models.i_geo_json_object import IGeoJSONObject
from datahub_lib.swagger_client.models.job_error import JobError
from datahub_lib.swagger_client.models.job_info import JobInfo
from datahub_lib.swagger_client.models.job_request import JobRequest
from datahub_lib.swagger_client.models.job_response import JobResponse
from datahub_lib.swagger_client.models.job_response_list_response import JobResponseListResponse
from datahub_lib.swagger_client.models.job_status import JobStatus
from datahub_lib.swagger_client.models.job_type_request import JobTypeRequest
from datahub_lib.swagger_client.models.job_type_response import JobTypeResponse
from datahub_lib.swagger_client.models.job_type_response_list_response import JobTypeResponseListResponse
from datahub_lib.swagger_client.models.location import Location
from datahub_lib.swagger_client.models.parameter import Parameter
from datahub_lib.swagger_client.models.partner_driver_timeline import PartnerDriverTimeline
from datahub_lib.swagger_client.models.partner_error import PartnerError
from datahub_lib.swagger_client.models.partner_limited_response import PartnerLimitedResponse
from datahub_lib.swagger_client.models.partner_limited_response_list_response import PartnerLimitedResponseListResponse
from datahub_lib.swagger_client.models.partner_request import PartnerRequest
from datahub_lib.swagger_client.models.partner_response import PartnerResponse
from datahub_lib.swagger_client.models.partner_status import PartnerStatus
from datahub_lib.swagger_client.models.permission import Permission
from datahub_lib.swagger_client.models.pipeline_details import PipelineDetails
from datahub_lib.swagger_client.models.pipeline_run import PipelineRun
from datahub_lib.swagger_client.models.polygon import Polygon
from datahub_lib.swagger_client.models.property_values import PropertyValues
from datahub_lib.swagger_client.models.query_result_page import QueryResultPage
from datahub_lib.swagger_client.models.role_assignment_request import RoleAssignmentRequest
from datahub_lib.swagger_client.models.role_assignment_response import RoleAssignmentResponse
from datahub_lib.swagger_client.models.role_assignment_response_list_response import RoleAssignmentResponseListResponse
from datahub_lib.swagger_client.models.role_definition_response import RoleDefinitionResponse
from datahub_lib.swagger_client.models.role_definition_response_list_response import RoleDefinitionResponseListResponse
from datahub_lib.swagger_client.models.rule_request import RuleRequest
from datahub_lib.swagger_client.models.rule_response import RuleResponse
from datahub_lib.swagger_client.models.rule_response_list_response import RuleResponseListResponse
from datahub_lib.swagger_client.models.scene_file_request import SceneFileRequest
from datahub_lib.swagger_client.models.scene_request import SceneRequest
from datahub_lib.swagger_client.models.scene_response import SceneResponse
from datahub_lib.swagger_client.models.scene_response_list_response import SceneResponseListResponse
from datahub_lib.swagger_client.models.sensor_measure import SensorMeasure
from datahub_lib.swagger_client.models.sensor_model_request import SensorModelRequest
from datahub_lib.swagger_client.models.sensor_model_response import SensorModelResponse
from datahub_lib.swagger_client.models.sensor_model_response_list_response import SensorModelResponseListResponse
from datahub_lib.swagger_client.models.sensor_request import SensorRequest
from datahub_lib.swagger_client.models.sensor_response import SensorResponse
from datahub_lib.swagger_client.models.sensor_response_list_response import SensorResponseListResponse
from datahub_lib.swagger_client.models.telemetry_query_filter import TelemetryQueryFilter
from datahub_lib.swagger_client.models.tsx import Tsx
from datahub_lib.swagger_client.models.weather_measure import WeatherMeasure
from datahub_lib.swagger_client.models.weather_station_model_request import WeatherStationModelRequest
from datahub_lib.swagger_client.models.weather_station_model_response import WeatherStationModelResponse
from datahub_lib.swagger_client.models.weather_station_model_response_list_response import WeatherStationModelResponseListResponse
from datahub_lib.swagger_client.models.weather_station_request import WeatherStationRequest
from datahub_lib.swagger_client.models.weather_station_response import WeatherStationResponse
from datahub_lib.swagger_client.models.weather_station_response_list_response import WeatherStationResponseListResponse
