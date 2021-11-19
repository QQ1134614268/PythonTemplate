# -*- coding:utf-8 -*-
"""
@Time: 2021/9/28
@Description:
"""
from os import path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

ROOT_DIR = path.abspath(path.dirname(__file__))
RESOURCE_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "resource")
DATA_DIR = path.join(path.dirname(path.dirname(ROOT_DIR)), "data")

LOG_PATH = DATA_DIR  # path.join(DATA_DIR, "log")

TIME_FMT = '%Y-%m-%d %H:%M:%S'
DEFAULT_TIME_STR = '%Y-%m-%d %H:%M:%S'
DEBUG_MODE = True

HOST = "127.0.0.1"
PORT = "3306"
USERNAME = 'root'
PASSWORD = "123456"
DB = "test"
DEBUG_MODE = True
url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DB)
engine = create_engine(url, echo=DEBUG_MODE)
session = sessionmaker(bind=engine)()
