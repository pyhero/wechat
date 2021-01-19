import datetime


class BaseWechat(object):
    def __init__(self, logger=None, debug=True):
        self._logger = logger
        self.debug = debug

    def logger(self, msg, level='debug', debug_switch=True):
        if not self.debug or not debug_switch:
            return

        if self._logger:
            getattr(self._logger, level)(msg)
        else:
            this_time = datetime.datetime.now().strftime("%Y-%m-%d %X.%f")
            print('{} {} {}'.format(this_time, level.upper(), msg))

    def convert_datetime_to_str(self, x, format_str='%Y-%m-%d %H:%M:%S'):
        if isinstance(x, datetime.datetime):
            return x.strftime(format_str)
        else:
            return x

    def convert_str_to_datetime(self, x, format_str='%Y-%m-%d %X.%f'):
        if isinstance(x, str):
            return datetime.datetime.strptime(x, format_str)
        else:
            return x
