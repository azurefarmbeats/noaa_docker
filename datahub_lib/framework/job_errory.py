"""
This File contains the custom errors
"""
from datahub_lib.framework.job_status_writer import JobStatusWriter


class JobError(RuntimeError):
    """
    This RuntimeError based class is used for throwing exceptions
    """
    INTERNAL_ERROR_SHORT = "500"
    INTERNAL_ERROR = "Job internal error"


    def __init__(self, value: object, code: str, is_transient):
        self.value = value or self.INTERNAL_ERROR
        self.code = str(code) or self.INTERNAL_ERROR_SHORT
        self.is_transient = is_transient

        # __str__ is to print() the value


    def __str__(self):
        return repr(self.value)


    @staticmethod
    def write_to_status_file(err: Exception, blob_url: str):
        """
        Writes given error info from exception to status file at blob_url.
        If given exception is of JobError type then richer info is written
        Otherwise only basic info
        Returns the status file contents as dict
        """
        writer = JobStatusWriter(blob_url)
        if isinstance(err, JobError):
            writer.set_error(err.code, err.value, err.is_transient)
        else:
            # Assume all unknown errors to be transient; err on the side of hope
            writer.set_error(JobError.INTERNAL_ERROR_SHORT,
                             JobError.INTERNAL_ERROR,
                             is_transient=True)
        return writer.flush()
