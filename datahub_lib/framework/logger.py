"""
Central logging utility class which controls logging related configuration

Usages:
first two lines in each python file will be following where logging is required
    from datahub_lib.framework.logger import Logger
    LOG = Logger.get_logger()
Then one can use `LOG` object to log debug, info, warning, error, exception, critical logs

Example:
    LOG.debug("[debug] Job created with id: {} type: {}".format("job-id", 0))

    LOG.info("[info] Logging with curly braces id: {} type: {{}}".format("job-id"))

    LOG.warning("[warning] Job created with id: {} python object: {}".format("job-id", "Any in-built python object"))

    LOG.error("[error] Job created with id: {} custom object: {}".format("job-id", "Any custom user-defined python object which implements __str__ or __repr__ method"))

    LOG.critical("[critical] Job created with id: {} type: {}".format("job-id", 0))

    try:
        raise Exception("my custom exception")
    except Exception:
        # This will print stack trace along with variables formatting
        LOG.exception("[exception] Caught exception while creating job with id: {} type: {}".format("job-id", 0))


"""
import os
import logging

from applicationinsights.channel import contracts
from applicationinsights.exceptions import enable
from applicationinsights.logging import LoggingHandler

from datahub_lib.framework.scene_constants import ENVIRONMENT_VARIABLE_LOG_LEVEL

LOGGING_LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

NONE_STRING = 'None'
LOGGER_NAME = 'farmbeats'


class Logger:
    """
    This class provide uniform logging format across whole project
    """
    @staticmethod
    def get_logger(unused_name=None):
        """
        Returns logger for given name
        """
        # TODO: fix all invocations with argument, appropriately.
        logger = logging.getLogger(LOGGER_NAME)
        logger.setLevel(Logger.get_logging_level())
        return logger


    @staticmethod
    def get_logging_level():
        '''
        Returns logging level using environment variable.
        '''
        #TODO: Read it from config file if available
        return LOGGING_LEVELS.get(
            os.environ.get(ENVIRONMENT_VARIABLE_LOG_LEVEL),
            logging.DEBUG)


    @staticmethod
    def attach_appinsights(logger, instrumentation_key: str):
        if not instrumentation_key:
            logger.warning("appinsights instrumentation key is null; not writing to app insights")
            return
            
        handler = LoggingHandler(instrumentation_key)

        # TODO: extend this collection to jobid, pipelineid or farmid etc.
        handler.client._context.properties['Collection'] = 'ADF_LOGS'

        # Removing all PIO information from context.
        # Due to a bug in LoggingHanlder constructor, its not honoring context passed.
        # so trying to set values once handler is created. Overriding with 'None' string
        # instead of None as for later value, its taking default value from constructor.
        handler.client._context.device = contracts.Device()
        handler.client._context.device.os_version = NONE_STRING
        handler.client._context.device.locale = NONE_STRING
        handler.client._context.device.id = NONE_STRING
        handler.client._context.device.type = NONE_STRING
        handler.client._context.device.oem_name = NONE_STRING
        handler.client._context.device.model = NONE_STRING

        handler.client._context.location = contracts.Location()
        handler.client._context.location.ip = NONE_STRING

        handler.client._context.user = contracts.User()
        handler.client._context.user.id = NONE_STRING
        handler.client._context.user.account_id = NONE_STRING
        handler.client._context.user.auth_user_id = NONE_STRING

        handler.client._context.session = contracts.Session()
        handler.client._context.session.id = NONE_STRING

        handler.client._context.cloud = contracts.Cloud()
        handler.client._context.cloud.role = NONE_STRING

        handler.setLevel(Logger.get_logging_level())

        # Log formatter looks similar to default python logging statement.
        handler.setFormatter(
            logging.Formatter(
                '[%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(process)d:%(thread)d]: %(message)s'))

        # enable exceptions to app insights
        enable(instrumentation_key)

        logger.addHandler(handler)
        logger.info("Attached app insights handler to logger")
