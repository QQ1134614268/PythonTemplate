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
DEBUG_MODE = True

LOG_PATH = DATA_DIR  # path.join(DATA_DIR, "log")

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_FORMAT = '%Y-%m-%d'
FILE_FORMAT = "%Y-%m-%d.%H-%M-%S.%f"

HOST = "127.0.0.1"
PORT = "3306"
USERNAME = 'root'
PASSWORD = "123456"
DB = "test"
localhost_test_url = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}?charset=utf8mb4'
localhost_test_engine = create_engine(localhost_test_url, echo=DEBUG_MODE)
localhost_test_session = sessionmaker(bind=localhost_test_engine)()

localhost_oa_url = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/oa?charset=utf8mb4'
localhost_oa_engine = create_engine(localhost_oa_url, echo=DEBUG_MODE)
localhost_oa_session = sessionmaker(bind=localhost_oa_engine)()

# Oracle db
ORACLE_NAME = "system"
ORACLE_PASSWORD = "oracle"
ORACLE_IP = "127.0.0.1"
ORACLE_PORT = "15210"
ORACLE_DB = "helowin"
oracle_url = f"oracle+cx_oracle://{ORACLE_NAME}:{ORACLE_PASSWORD}@{ORACLE_IP}:{ORACLE_PORT}/?service_name={ORACLE_DB}"
oracle_engine = create_engine(oracle_url)

time_zone = "%2B10:00"
time_zone_url = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/test?time_zone={time_zone}'

GGOK_ZOOKEEPER_HOST = "ggok.top:2181"
