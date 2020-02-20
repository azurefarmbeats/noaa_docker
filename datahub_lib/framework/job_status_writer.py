'''
Class to write job status json to a given blob.
'''
# System imports
import os
import tempfile
import json

# Local imports
from datahub_lib.framework.logger import Logger
from datahub_lib.helpers.utils.blob_util import BlobUtil

LOG = Logger.get_logger()

# Tag names in json
_OUTPUT = "output"
_IS_SUCCESS = "isSuccess"
_ERROR = "error"
_ERROR_CODE = "code"
_ERROR_MESSAGE = "message"
_ERROR_IS_TRANSIENT = "isTransient"
_PROGRESS_PERC = "progressPercentage"

class JobStatusWriter:
    '''
    Class to write job status to a given blob.  For use by code that runs as
    custom activity in ADF pipelines that are part of farmbeats job management
    system.

    Example usage:
        writer = JobStatusWriter(blob_url_with_sas_token)
        writer.init()
        writer.set_success(true)
        writer.set_progress(100)
        writer.set_error(100, "Internal message", True)
        writer.flush()

    Following in example of the contents of a job-status json file which this
    code updates.

    {
        "isSuccess": false,
        "error": {
            "code": "WrongUserNamePassword",
            "message": "Sentinel-2 username and password combination is wrong",
            "isTransient": false
        },
        "progressPercentage": 25,
        "output": {
            "tiles": [ "44QKF",  "46QKF" ],
            "scenesTotalCount": 150,
            "scenesDownloadedCount": 10,
            "childJobId2": {
                ...
            }
        }
    }
    '''
    class OutputWriter:
        '''
        Helper class to write to the output section of job status
        '''
        def __init__(self, job_writer):
            self.job_writer = job_writer


        @staticmethod
        def _get_output(status: dict) -> dict:
            '''
            Helper to get outut section of status; adds if it doesn't exist
            '''
            # Initialize _OUTPUT property - it may be None or not exist at all.
            if _OUTPUT not in status or status[_OUTPUT] is None:
                status[_OUTPUT] = dict()
            return status[_OUTPUT]


        def set_prop(self, prop: str, value):
            '''
            Sets/Overwrites property with given name and value.
            value can be string, int, float, list or dict
            '''
            def __func__(status: dict):
                output = JobStatusWriter.OutputWriter._get_output(status)

                if prop in output and output[prop] == value:
                    return False
                else:
                    output[prop] = value
                    return True

            self.job_writer._actions.append(__func__)


        def add_to_list(self, prop: str, values: list):
            '''
            Adds given values to a list property.  If property doesn't exist,
            a new one is added.  If it exists, it must of list type.
            '''
            def __func__(status: dict):
                output = JobStatusWriter.OutputWriter._get_output(status)
                new_list = output[prop] if prop in output else list()
                new_list.extend(values or [])
                output[prop] = new_list
                return True

            self.job_writer._actions.append(__func__)


        def increment(self, prop: str, value):
            '''
            Increments value of given property by given value.  If property
            doesn't exist, it is set to given value.
            Property must of integral type (int or float).  The end-value would
            be float iff either of the current value of property or the given
            value are float
            '''
            def __func__(status: dict):
                output = JobStatusWriter.OutputWriter._get_output(status)
                old_value = output[prop] if prop in output else 0
                new_value = old_value + value
                output[prop] = new_value
                return True

            self.job_writer._actions.append(__func__)


    def __init__(self, sas_blob_url: str):
        '''
        Constructor
        :param str blob_url: blob url with sas token for writing
        '''
        self.__output_writer = JobStatusWriter.OutputWriter(self)
        self.__sas_blob_url = sas_blob_url
        self._actions = []


    def set_success(self, value: bool):
        '''
        Sets the isSuccess property to given value.  Overwrites any existing
        value.
        '''
        def __func__(status: dict) -> bool:
            if _IS_SUCCESS in status and status[_IS_SUCCESS] == value:
                return False
            else:
                status[_IS_SUCCESS] = value
                return True

        self._actions.append(__func__)


    def set_error(self, code: str, message: str, is_transient: bool = True):
        '''
        Sets the error property dict with given values.  Overwrites any existing
        value except when the old value of is_transient is false and its new
        value is true
        '''
        def __func__(status: dict) -> bool:
            # Initialize _ERROR property - it may be None or not exist at all
            if _ERROR not in status or status[_ERROR] is None:
                status[_ERROR] = dict()

            if _ERROR_IS_TRANSIENT in status[_ERROR] and \
                not status[_ERROR][_ERROR_IS_TRANSIENT] and is_transient:
                return False
            else:
                status[_ERROR][_ERROR_CODE] = code
                status[_ERROR][_ERROR_MESSAGE] = message
                status[_ERROR][_ERROR_IS_TRANSIENT] = is_transient
                return True

        self._actions.append(__func__)


    def set_progress(self, value: int, do_increment: bool = False):
        '''
        Sets or increments progress percentage to/by given value.
        Sets if increment if false; increments otherwise.
        Value can be negative
        '''
        def __func__(status: dict) -> bool:
            orig_perc = status[_PROGRESS_PERC] if _PROGRESS_PERC in status else None
            new_perc = ((orig_perc or 0) + value) if do_increment else value
            if orig_perc == new_perc:
                return False
            else:
                # Ensure that the end value is within range 0-100??
                status[_PROGRESS_PERC] = new_perc
                return True

        self._actions.append(__func__)


    def get_output_writer(self):
        '''
        Returns writer for writing to the output section of job status
        '''
        return self.__output_writer


    def flush(self):
        '''
        Flushes change to job status file if needed
        :return: returns updated job status
        :rtype: dict
        '''
        # Clear _actions; we don't want another call to this method to execute
        # them again.
        actions = self._actions
        self._actions = []

        # 9 attempts at writing
        n_max = 9
        for i in range(n_max):
            # Read status from self.__sas_blob_url blob
            # self.__sas_blob_url blob may be None (used only for testing)

            # Initialize it with the exactly value job-driver does so
            status = {
                _IS_SUCCESS : None,
                _PROGRESS_PERC : None,
                _ERROR: None,
                _OUTPUT : None
            }
            if self.__sas_blob_url:
                tmp_dir = tempfile.TemporaryDirectory().name
                os.makedirs(tmp_dir, exist_ok=True)
                job_output_file, etag = BlobUtil.download_using_sas_url(self.__sas_blob_url, tmp_dir)
                status = dict()
                with open(job_output_file, 'r') as f:
                    status = json.loads(f.read())


            # Apply updates
            do_update = False
            for updater in actions:
                do_update = updater(status) or do_update

            if not do_update:
                return status
            else:
                try:
                    # write status back to blob
                    if self.__sas_blob_url:
                        with open(job_output_file, 'w') as f:
                            json.dump(status, f, indent=4)
                        response = BlobUtil.upload_using_sas_url(self.__sas_blob_url,
                                                                 job_output_file,
                                                                 etag=etag)
                    return status
                # Currently the python SDK for blob does not give client the status code in case of
                # failure. So, we are catching general exception and re-trying.
                # TODO: If it gets fixed, retry only if http response code is 412.
                except Exception as e:
                    LOG.exception('Attempt #{}: failed to write job status to blob. \n Error:{}'.format(i+1, e))

        # Unable to write after all the attempts
        err_msg = "Unable to update status after {} attempts"
        raise RuntimeError(err_msg.format(n_max))


class JobStatusWriterHelper:
    '''
    Helper methods to use JobStatusWriter
    '''
    @staticmethod
    def increment_output_tag(status_blob_url: str, tag: str, value):
        '''
        Reads file, increments value of given tag by value and saves
        '''
        if status_blob_url:
            writer = JobStatusWriter(status_blob_url)
            out_writer = writer.get_output_writer()
            out_writer.increment(tag, value)
            writer.flush()

    @staticmethod
    def set_success_flag(status_blob_url: str, value: bool):
        '''
        Reads file, sets value of the isSuccess flag
        '''
        if status_blob_url:
            writer = JobStatusWriter(status_blob_url)
            writer.set_success(value)
            writer.flush()
