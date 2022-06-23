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

TIME_FMT = '%Y-%m-%d %H:%M:%S'
DEFAULT_TIME_STR = '%Y-%m-%d %H:%M:%S'

HOST = "127.0.0.1"
PORT = "3306"
USERNAME = 'root'
PASSWORD = "123456"
DB = "test"
localhost_test_url = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOST, PORT, DB)
localhost_test_engine = create_engine(localhost_test_url, echo=DEBUG_MODE)
localhost_test_session = sessionmaker(bind=localhost_test_engine)()

# Oracle db
ORACLE_NAME = "system"
ORACLE_PASSWORD = "oracle"
ORACLE_IP = "127.0.0.1"
ORACLE_PORT = "15210"
ORACLE_DB = "helowin"
oracle_url = "oracle+cx_oracle://{}:{}@{}:{}/?service_name={}".format(
    ORACLE_NAME, ORACLE_PASSWORD, ORACLE_IP, ORACLE_PORT, ORACLE_DB)
oracle_engine = create_engine(oracle_url)

# sqlserver db
sqlserver_ip = "127.0.0.1"
sqlserver_db = "WindDB"
sqlserver_username = "sa"
sqlserver_password = "123456"
sqlserver_url = 'mssql+pymssql://{}:{}@{}/{}'.format(sqlserver_username, sqlserver_password, sqlserver_ip, sqlserver_db)
sqlserver_engine = create_engine(sqlserver_url)

time_zone_url = 'mysql+mysqlconnector://{}:{}@{}/{}?time_zone={}'.format(
    'root', "123456", "127.0.0.1", 'test', "%2B10:00")

GGOK_ZOOKEEPER_HOST = "ggok.top:2181"
