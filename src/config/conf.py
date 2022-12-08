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

DEBUG_MODE = True

FILE_FORMAT = "%Y-%m-%d_%H-%M-%S_%f"

GGOK_ZOOKEEPER_HOST = "ggok.top:2181"
