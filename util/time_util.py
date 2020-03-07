# -*- coding:utf-8 -*-
import datetime

import time

default_time_str = '%Y_%m_%d_%H_%M_%S_%f'


def getUtcTimeStr():
    return datetime.datetime.utcnow().strftime(default_time_str)


def getDatetimeByStr(time_str):
    return datetime.datetime.strptime(time_str, default_time_str)


def utcToLocal():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=8)


def getUtc():
    return datetime.datetime.utcnow()


if __name__ == '__main__':
    print(datetime.datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f'))
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(datetime.datetime.now())
