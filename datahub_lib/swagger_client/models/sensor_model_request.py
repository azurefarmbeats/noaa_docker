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


class SensorModelRequest(object):
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
        'type': 'str',
        'manufacturer': 'str',
        'product_code': 'str',
        'sensor_measures': 'list[SensorMeasure]',
        'name': 'str',
        'description': 'str',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'manufacturer': 'manufacturer',
        'product_code': 'productCode',
        'sensor_measures': 'sensorMeasures',
        'name': 'name',
        'description': 'description',
        'properties': 'properties'
    }

    def __init__(self, type=None, manufacturer=None, product_code=None, sensor_measures=None, name=None, description=None, properties=None):  # noqa: E501
        """SensorModelRequest - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._manufacturer = None
        self._product_code = None
        self._sensor_measures = None
        self._name = None
        self._description = None
        self._properties = None
        self.discriminator = None

        self.type = type
        if manufacturer is not None:
            self.manufacturer = manufacturer
        self.product_code = product_code
        self.sensor_measures = sensor_measures
        self.name = name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties

    @property
    def type(self):
        """Gets the type of this SensorModelRequest.  # noqa: E501

        Gets or sets type of the sensor.  # noqa: E501

        :return: The type of this SensorModelRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SensorModelRequest.

        Gets or sets type of the sensor.  # noqa: E501

        :param type: The type of this SensorModelRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Analog", "Digital"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def manufacturer(self):
        """Gets the manufacturer of this SensorModelRequest.  # noqa: E501

        Gets or sets manufacturer of the sensor.  # noqa: E501

        :return: The manufacturer of this SensorModelRequest.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this SensorModelRequest.

        Gets or sets manufacturer of the sensor.  # noqa: E501

        :param manufacturer: The manufacturer of this SensorModelRequest.  # noqa: E501
        :type: str
        """
        if manufacturer is not None and len(manufacturer) > 200:
            raise ValueError("Invalid value for `manufacturer`, length must be less than or equal to `200`")  # noqa: E501
        if manufacturer is not None and len(manufacturer) < 1:
            raise ValueError("Invalid value for `manufacturer`, length must be greater than or equal to `1`")  # noqa: E501

        self._manufacturer = manufacturer

    @property
    def product_code(self):
        """Gets the product_code of this SensorModelRequest.  # noqa: E501

        Gets or sets sensor product code or Model Name/Number.  eg: RS-CO2-N01.  # noqa: E501

        :return: The product_code of this SensorModelRequest.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this SensorModelRequest.

        Gets or sets sensor product code or Model Name/Number.  eg: RS-CO2-N01.  # noqa: E501

        :param product_code: The product_code of this SensorModelRequest.  # noqa: E501
        :type: str
        """
        if product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501
        if product_code is not None and len(product_code) > 200:
            raise ValueError("Invalid value for `product_code`, length must be less than or equal to `200`")  # noqa: E501
        if product_code is not None and len(product_code) < 1:
            raise ValueError("Invalid value for `product_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._product_code = product_code

    @property
    def sensor_measures(self):
        """Gets the sensor_measures of this SensorModelRequest.  # noqa: E501

        Gets or sets list of Measurements supported by sensor.  # noqa: E501

        :return: The sensor_measures of this SensorModelRequest.  # noqa: E501
        :rtype: list[SensorMeasure]
        """
        return self._sensor_measures

    @sensor_measures.setter
    def sensor_measures(self, sensor_measures):
        """Sets the sensor_measures of this SensorModelRequest.

        Gets or sets list of Measurements supported by sensor.  # noqa: E501

        :param sensor_measures: The sensor_measures of this SensorModelRequest.  # noqa: E501
        :type: list[SensorMeasure]
        """
        if sensor_measures is None:
            raise ValueError("Invalid value for `sensor_measures`, must not be `None`")  # noqa: E501

        self._sensor_measures = sensor_measures

    @property
    def name(self):
        """Gets the name of this SensorModelRequest.  # noqa: E501

        Gets or sets name to identify resource.  # noqa: E501

        :return: The name of this SensorModelRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SensorModelRequest.

        Gets or sets name to identify resource.  # noqa: E501

        :param name: The name of this SensorModelRequest.  # noqa: E501
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
        """Gets the description of this SensorModelRequest.  # noqa: E501

        Gets or sets textual description of resource.  # noqa: E501

        :return: The description of this SensorModelRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SensorModelRequest.

        Gets or sets textual description of resource.  # noqa: E501

        :param description: The description of this SensorModelRequest.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if description is not None and len(description) < 3:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `3`")  # noqa: E501

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this SensorModelRequest.  # noqa: E501

        Gets or sets additional properties of the resource.  # noqa: E501

        :return: The properties of this SensorModelRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SensorModelRequest.

        Gets or sets additional properties of the resource.  # noqa: E501

        :param properties: The properties of this SensorModelRequest.  # noqa: E501
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
        if issubclass(SensorModelRequest, dict):
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
        if not isinstance(other, SensorModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
