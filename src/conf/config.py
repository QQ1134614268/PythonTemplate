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
sqlserver_password = "123456"
sqlserver_user = "sa"
sqlserver_url = 'mssql+pymssql://{}:{}@{}/{}'.format(sqlserver_user, sqlserver_password, sqlserver_ip, sqlserver_db)
sqlserver_engine = create_engine(sqlserver_url)
localhost_world_url = "mysql+mysqlconnector://wg:123456@ggok.top:3306/world?charset=utf8"
localhost_test_url = "mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8"
time_zone_url = 'mysql+mysqlconnector://{}:{}@{}/{}?time_zone={}'.format(
    'root', "123456", "127.0.0.1", 'test', "%2B10:00")
