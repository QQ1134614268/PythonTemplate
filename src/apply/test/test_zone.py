# -*- coding:utf-8 -*-
"""
@Time: 2021/12/15
@Description:
"""
from datetime import tzinfo, timedelta, datetime
from unittest import TestCase

from conf.config import DEFAULT_TIME_STR


class UTC(tzinfo):
    """UTC"""

    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)


class TestMysql(TestCase):

    def test_session(self):
        # 格式化构造时间, 2021-12-01 12:00:00
        new_time = datetime(2021, 12, 1, 12, 00, 00)
        print(new_time.strftime(DEFAULT_TIME_STR))

        # now 获取系统时间, fmt 受时区影响
        new_time = datetime.now()
        print(new_time.strftime(DEFAULT_TIME_STR))
