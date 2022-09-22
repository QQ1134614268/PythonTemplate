from datetime import datetime

from conf.time_conf import DATE_TIME_FORMAT


# 字符串转时间
def get_datetime_by_str(time_str, fmt=DATE_TIME_FORMAT):
    return datetime.strptime(time_str, fmt)


# 时间转字符串
def get_str_by_datetime(fmt=DATE_TIME_FORMAT):
    return datetime.now().strftime(fmt)


def get_now_str(fmt=DATE_TIME_FORMAT):
    return datetime.now().strftime(fmt)


def get_now():
    return datetime.now()
