'''
The module has date related helper methods.
'''
from datetime import date, datetime


class DateTimeUtil:
    '''
    Contains useful date and time related utils
    '''


    @staticmethod
    def to_datetime(in_obj):
        '''
        Parses given input in the form of a date, datetime or a string and
        returns a datetime object. Parses a variety of commonly seen string
        formats. Raises ValueError on invalid input string
        :param in_obj: a date, datetime or string in a variety of formats
        :return: a DateTime object
        '''

        if isinstance(in_obj, datetime):
            return in_obj
        elif isinstance(in_obj, date):
            return datetime(in_obj.year, in_obj.month, in_obj.day)
        elif isinstance(in_obj, str):
            formats = [
                '%Y.%m.%d',
                '%Y-%m-%d',
                '%Y%m%d',
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%d %H:%M:%S.%f',
                '%Y-%m-%d %H:%M:%S%z',
                '%Y-%m-%d %H:%M:%S.%f%z',
                '%Y-%m-%dT%H:%M:%SZ',
                '%Y-%m-%dT%H:%M:%S.%fZ', 
                '%Y-%m-%dT%H:%M:%S.%fffZ', 
                '%Y-%m-%dT%H:%M:%S.%ffffffZ', 
                '%Y-%m-%dT%H:%M:%S.%fffffffZ'
                ]
            for fmt in formats:
                try:
                    return datetime.strptime(in_obj, fmt)
                except ValueError:
                    pass

            raise ValueError('Invalid date string %s' % in_obj)
        else:
            raise ValueError('Unknown input type')


    @staticmethod
    def get_timestamp(date_obj: datetime) -> int:
        '''
        Get timestamp in seconds precision from a datetime object
        :param date_obj:
        :return:
        '''
        return int(round(date_obj.timestamp()))


    @staticmethod
    def equals(date1: datetime, date2: datetime) -> bool:
        '''
        Checks equality of two datetime objects with precise only to the milliseconds
        :param date1:
        :param date2:
        :return: True if both are equal False otherwise
        '''
        if not date1 and not date2:
            return True
        if (date1 and not date2) or (not date1 and date2):
            return False
        return DateTimeUtil.get_timestamp(date1) == DateTimeUtil.get_timestamp(date2)
