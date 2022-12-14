# -*- coding:utf-8 -*-
"""
@Time: 2021/3/14
@Description:
"""
import decimal
import json
import uuid
from datetime import date, datetime
from enum import Enum

from config.time_conf import DATE_TIME_FORMAT, DATE_FORMAT


class MyJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Enum):
            return o.name
        if isinstance(o, datetime):
            return o.strftime(DATE_TIME_FORMAT)
        if isinstance(o, date):
            return o.strftime(DATE_FORMAT)
        if isinstance(o, (decimal.Decimal, uuid.UUID)):
            return str(o)
        if hasattr(o, "__dict__"):
            return o.__dict__
        # return str(o)
        return super().default(o)
