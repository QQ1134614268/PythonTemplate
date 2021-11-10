# -*- coding:utf-8 -*-
"""
@Time: 2021/9/28
@Description:
"""
from os import path

ROOT_DIR = path.abspath(path.dirname(__file__))
RESOURCE_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "resource")
DATA_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "data")

LOG_PATH = DATA_DIR  # path.join(DATA_DIR, "log")

TIME_FMT = '%Y-%m-%d %H:%M:%S'
DEFAULT_TIME_STR = '%Y-%m-%d %H:%M:%S'
DEBUG_MODE = True
