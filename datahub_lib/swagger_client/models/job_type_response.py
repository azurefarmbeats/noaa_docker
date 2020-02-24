# coding: utf-8

"""
    Azure FarmBeats API

    <p>  <p>Azure FarmBeats helps you build digital agricultural solutions in Azure. By providing a standardized schema to query agricultural data from various sources, Azure FarmBeats provides you:  <ul >   <li style=\"margin: 7px;\">Ability to acquire, aggregate, process and store agricultural data.</li>   <li style=\"margin: 7px;\">Capability to fuse data between data sources and generate insights.</li>   <li style=\"margin: 7px;\">Schematized access and query capabilities on ingested data.</li>  </ul>  </p>  <h><b>REST Operation Groups</b></h>  <p><b>Farm:</b></p>  <p>Farm corresponds to a physical location of interest within the system. Each Farm has a Farm name and a unique farm id.</p>  <p><b>Device:</b></p>  <p>Device corresponds to a physical device present in the farm. Each device has a unique device id. Device is typically provisioned to a farm with a farm id.</p>  <p><b>DeviceModel:</b></p>  <p>DeviceModel corresponds to the meta-data of the device such as the Manufacturer, Type of the device either Gateway or Node.</p>  <p><b>Sensor:</b></p>  <p>Sensor corresponds to a physical sensor that records values. A sensor is typically connected to a device with a device id.</p>  </p>  <p><b>SensorModel:</b></p>  <p>SensorModel corresponds to the meta-data of the sensor such as the Manufacturer, Type of the sensor either Analog or Digital, Sensor Measure such as Ambient Temperature, Pressure etc.</p>  <p><b>Telemetry:</b></p>  <p>Telemetry provides the ability to read telemetry messages for a particular sensor & time range.</p>  <p><b>Job:</b></p>  <p>Job corresponds to any workflow of activities which are executed in the system to get a desired output. Each job is associated with a job id and job type.</p>  <p><b>JobType:</b></p>  <p>JobType corresponds to different job types supported by the system. This includes system defined & user-defined job types.</p>  <p><b>ExtendedType:</b></p>  <p>ExtendedType corresponds to the list of system & user-defined types in the system. This helps setup a new Sensor or Scene or Scenefile type in the system.</p>  <p><b>Partner:</b></p>  <p>Partner corresponds to the sensor/weather/imagery integration partner.</p>  <p><b>Scene:</b></p>  <p>Scene corresponds to any generated output in the context of a Farm. Each Scene has a scene id, scene source, scene type and farm id associated with it. Each scene id  can have multiple scene files associated with it.</p>  <p><b>SceneFile:</b></p>  <p>SceneFile corresponds to all files which are generated for single scene. A single scene id can have multiple SceneFile ids associated with it.</p>  <p><b>Rule:</b></p>  <p>Rule corresponds to a condition for farm-related data to trigger an alert. Each rule will be in the context of a farm's data.</p>  <p><b>Alert:</b></p>  <p>Alert corresponds to a notification which gets generated when a rule condition is met. Each alert will be in the context of a rule.</p>  <p><b>RoleDefinition:</b></p>  <p>RoleDefinition defines allowed and disallowed actions for a role.</p>  <p><b>RoleAssignment:</b></p>  <p>RoleAssignment corresponds to the assignment of a role to a user or a service principal.</p>  </p>    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobTypeResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'is_partner_job_type': 'bool',
        'status': 'str',
        'error_message': 'str',
        'created_at': 'datetime',
        'last_modified_at': 'datetime',
        'pipeline_details': 'PipelineDetails',
        'name': 'str',
        'description': 'str',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'is_partner_job_type': 'isPartnerJobType',
        'status': 'status',
        'error_message': 'errorMessage',
        'created_at': 'createdAt',
        'last_modified_at': 'lastModifiedAt',
        'pipeline_details': 'pipelineDetails',
        'name': 'name',
        'description': 'description',
        'properties': 'properties'
    }

    def __init__(self, id=None, is_partner_job_type=None, status=None, error_message=None, created_at=None, last_modified_at=None, pipeline_details=None, name=None, description=None, properties=None):  # noqa: E501
        """JobTypeResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._is_partner_job_type = None
        self._status = None
        self._error_message = None
        self._created_at = None
        self._last_modified_at = None
        self._pipeline_details = None
        self._name = None
        self._description = None
        self._properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_partner_job_type is not None:
            self.is_partner_job_type = is_partner_job_type
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message
        if created_at is not None:
            self.created_at = created_at
        if last_modified_at is not None:
            self.last_modified_at = last_modified_at
        if pipeline_details is not None:
            self.pipeline_details = pipeline_details
        self.name = name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties

    @property
    def id(self):
        """Gets the id of this JobTypeResponse.  # noqa: E501

        Gets or sets unique id of job type.  # noqa: E501

        :return: The id of this JobTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobTypeResponse.

        Gets or sets unique id of job type.  # noqa: E501

        :param id: The id of this JobTypeResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_partner_job_type(self):
        """Gets the is_partner_job_type of this JobTypeResponse.  # noqa: E501

        Gets or sets a value indicating whether it's a partner JobType or not.  # noqa: E501

        :return: The is_partner_job_type of this JobTypeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_partner_job_type

    @is_partner_job_type.setter
    def is_partner_job_type(self, is_partner_job_type):
        """Sets the is_partner_job_type of this JobTypeResponse.

        Gets or sets a value indicating whether it's a partner JobType or not.  # noqa: E501

        :param is_partner_job_type: The is_partner_job_type of this JobTypeResponse.  # noqa: E501
        :type: bool
        """

        self._is_partner_job_type = is_partner_job_type

    @property
    def status(self):
        """Gets the status of this JobTypeResponse.  # noqa: E501

        Gets or sets status of JobType.  This status represents whether or not corresponding ADF pipeline has been successfully created.  # noqa: E501

        :return: The status of this JobTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobTypeResponse.

        Gets or sets status of JobType.  This status represents whether or not corresponding ADF pipeline has been successfully created.  # noqa: E501

        :param status: The status of this JobTypeResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Waiting", "Provisioning", "Failed", "PendingRetry", "Ready"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this JobTypeResponse.  # noqa: E501

        Gets or sets error message.  Helps in debugging for the Partner JobTypes.  # noqa: E501

        :return: The error_message of this JobTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this JobTypeResponse.

        Gets or sets error message.  Helps in debugging for the Partner JobTypes.  # noqa: E501

        :param error_message: The error_message of this JobTypeResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def created_at(self):
        """Gets the created_at of this JobTypeResponse.  # noqa: E501

        Gets or sets created date.  # noqa: E501

        :return: The created_at of this JobTypeResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this JobTypeResponse.

        Gets or sets created date.  # noqa: E501

        :param created_at: The created_at of this JobTypeResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this JobTypeResponse.  # noqa: E501

        Gets or sets last modified date.  # noqa: E501

        :return: The last_modified_at of this JobTypeResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this JobTypeResponse.

        Gets or sets last modified date.  # noqa: E501

        :param last_modified_at: The last_modified_at of this JobTypeResponse.  # noqa: E501
        :type: datetime
        """

        self._last_modified_at = last_modified_at

    @property
    def pipeline_details(self):
        """Gets the pipeline_details of this JobTypeResponse.  # noqa: E501

        Gets or sets azure Data Factory pipeline specific details.  # noqa: E501

        :return: The pipeline_details of this JobTypeResponse.  # noqa: E501
        :rtype: PipelineDetails
        """
        return self._pipeline_details

    @pipeline_details.setter
    def pipeline_details(self, pipeline_details):
        """Sets the pipeline_details of this JobTypeResponse.

        Gets or sets azure Data Factory pipeline specific details.  # noqa: E501

        :param pipeline_details: The pipeline_details of this JobTypeResponse.  # noqa: E501
        :type: PipelineDetails
        """

        self._pipeline_details = pipeline_details

    @property
    def name(self):
        """Gets the name of this JobTypeResponse.  # noqa: E501

        Gets or sets name to identify resource.  # noqa: E501

        :return: The name of this JobTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobTypeResponse.

        Gets or sets name to identify resource.  # noqa: E501

        :param name: The name of this JobTypeResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this JobTypeResponse.  # noqa: E501

        Gets or sets textual description of resource.  # noqa: E501

        :return: The description of this JobTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobTypeResponse.

        Gets or sets textual description of resource.  # noqa: E501

        :param description: The description of this JobTypeResponse.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if description is not None and len(description) < 3:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `3`")  # noqa: E501

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this JobTypeResponse.  # noqa: E501

        Gets or sets additional properties of the resource.  # noqa: E501

        :return: The properties of this JobTypeResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this JobTypeResponse.

        Gets or sets additional properties of the resource.  # noqa: E501

        :param properties: The properties of this JobTypeResponse.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(JobTypeResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
