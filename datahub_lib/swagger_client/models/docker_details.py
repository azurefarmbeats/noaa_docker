# coding: utf-8

"""
    Azure FarmBeats API

    <p> <p>Azure FarmBeats helps you build digital agricultural solutions in Azure. By providing a standardized schema to query agricultural data from various sources, Azure FarmBeats provides you: <ul >  <li style=\"margin: 7px;\">Ability to acquire, aggregate, process and store agricultural data.</li>  <li style=\"margin: 7px;\">Capability to fuse data between data sources and generate insights.</li>  <li style=\"margin: 7px;\">Schematized access and query capabilities on ingested data.</li> </ul> </p> <h><b>REST Operation Groups</b></h> <p><b>Farm:</b></p> <p>Farm corresponds to a physical location of interest within the system. Each Farm has a Farm name and a unique farm id.</p> <p><b>Device:</b></p> <p>Device corresponds to a physical device present in the farm. Each device has a unique device id. Device is typically provisioned to a farm with a farm id.</p> <p><b>DeviceModel:</b></p> <p>DeviceModel corresponds to the meta-data of the device such as the Manufacturer, Type of the device either Gateway or Node.</p> <p><b>Sensor:</b></p> <p>Sensor corresponds to a physical sensor that records values. A sensor is typically connected to a device with a device id.</p> </p> <p><b>SensorModel:</b></p> <p>SensorModel corresponds to the meta-data of the sensor such as the Manufacturer, Type of the sensor either Analog or Digital, Sensor Measure such as Ambient Temperature, Pressure etc.</p> <p><b>Telemetry:</b></p> <p>Telemetry provides the ability to read telemetry messages for a particular sensor & time range.</p> <p><b>Job:</b></p> <p>Job corresponds to any workflow of activities which are executed in the system to get a desired output. Each job is associated with a job id and job type.</p> <p><b>JobType:</b></p> <p>JobType corresponds to different job types supported by the system. This includes system defined & user-defined job types.</p> <p><b>ExtendedType:</b></p> <p>ExtendedType corresponds to the list of system & user-defined types in the system. This helps setup a new Sensor or Scene or Scenefile type in the system.</p> <p><b>Partner:</b></p> <p>Partner corresponds to the sensor/weather/imagery integration partner.</p> <p><b>Scene:</b></p> <p>Scene corresponds to any generated output in the context of a Farm. Each Scene has a scene id, scene source, scene type and farm id associated with it. Each scene id  can have multiple scene files associated with it.</p> <p><b>SceneFile:</b></p> <p>SceneFile corresponds to all files which are generated for single scene. A single scene id can have multiple SceneFile ids associated with it.</p> <p><b>Rule:</b></p> <p>Rule corresponds to a condition for farm-related data to trigger an alert. Each rule will be in the context of a farm's data.</p> <p><b>Alert:</b></p> <p>Alert corresponds to a notification which gets generated when a rule condition is met. Each alert will be in the context of a rule.</p> <p><b>RoleDefinition:</b></p> <p>RoleDefinition defines allowed and disallowed actions for a role.</p> <p><b>RoleAssignment:</b></p> <p>RoleAssignment corresponds to the assignment of a role to a user or a service principal.</p> </p>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from datahub_lib.swagger_client.configuration import Configuration


class DockerDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'credentials': 'Credentials',
        'image_name': 'str',
        'image_tag': 'str',
        'azure_batch_vm_details': 'AzureBatchDetails'
    }

    attribute_map = {
        'credentials': 'credentials',
        'image_name': 'imageName',
        'image_tag': 'imageTag',
        'azure_batch_vm_details': 'azureBatchVMDetails'
    }

    def __init__(self, credentials=None, image_name=None, image_tag=None, azure_batch_vm_details=None, local_vars_configuration=None):  # noqa: E501
        """DockerDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._credentials = None
        self._image_name = None
        self._image_tag = None
        self._azure_batch_vm_details = None
        self.discriminator = None

        if credentials is not None:
            self.credentials = credentials
        self.image_name = image_name
        self.image_tag = image_tag
        self.azure_batch_vm_details = azure_batch_vm_details

    @property
    def credentials(self):
        """Gets the credentials of this DockerDetails.  # noqa: E501


        :return: The credentials of this DockerDetails.  # noqa: E501
        :rtype: Credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this DockerDetails.


        :param credentials: The credentials of this DockerDetails.  # noqa: E501
        :type: Credentials
        """

        self._credentials = credentials

    @property
    def image_name(self):
        """Gets the image_name of this DockerDetails.  # noqa: E501

        Gets or sets docker image name.  # noqa: E501

        :return: The image_name of this DockerDetails.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this DockerDetails.

        Gets or sets docker image name.  # noqa: E501

        :param image_name: The image_name of this DockerDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image_name is None:  # noqa: E501
            raise ValueError("Invalid value for `image_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_name is not None and len(image_name) > 300):
            raise ValueError("Invalid value for `image_name`, length must be less than or equal to `300`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_name is not None and len(image_name) < 3):
            raise ValueError("Invalid value for `image_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._image_name = image_name

    @property
    def image_tag(self):
        """Gets the image_tag of this DockerDetails.  # noqa: E501

        Gets or sets docker image tag.  # noqa: E501

        :return: The image_tag of this DockerDetails.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this DockerDetails.

        Gets or sets docker image tag.  # noqa: E501

        :param image_tag: The image_tag of this DockerDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image_tag is None:  # noqa: E501
            raise ValueError("Invalid value for `image_tag`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_tag is not None and len(image_tag) > 300):
            raise ValueError("Invalid value for `image_tag`, length must be less than or equal to `300`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_tag is not None and len(image_tag) < 3):
            raise ValueError("Invalid value for `image_tag`, length must be greater than or equal to `3`")  # noqa: E501

        self._image_tag = image_tag

    @property
    def azure_batch_vm_details(self):
        """Gets the azure_batch_vm_details of this DockerDetails.  # noqa: E501


        :return: The azure_batch_vm_details of this DockerDetails.  # noqa: E501
        :rtype: AzureBatchDetails
        """
        return self._azure_batch_vm_details

    @azure_batch_vm_details.setter
    def azure_batch_vm_details(self, azure_batch_vm_details):
        """Sets the azure_batch_vm_details of this DockerDetails.


        :param azure_batch_vm_details: The azure_batch_vm_details of this DockerDetails.  # noqa: E501
        :type: AzureBatchDetails
        """
        if self.local_vars_configuration.client_side_validation and azure_batch_vm_details is None:  # noqa: E501
            raise ValueError("Invalid value for `azure_batch_vm_details`, must not be `None`")  # noqa: E501

        self._azure_batch_vm_details = azure_batch_vm_details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DockerDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerDetails):
            return True

        return self.to_dict() != other.to_dict()
