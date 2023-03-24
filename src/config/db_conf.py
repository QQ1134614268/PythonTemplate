# -*- coding:utf-8 -*-
"""
@Time: 2022/9/22
@Description:
"""
from config.conf import DEBUG_MODE

from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOST = "127.0.0.1"
PORT = "3306"
USERNAME = 'root'
PASSWORD = "123456"
DB = "test"
localhost_test_url = f'mysql+mysqlconnector://{quote(USERNAME)}:{quote(PASSWORD)}@{HOST}:{PORT}/{DB}?charset=utf8mb4'
localhost_test_engine = create_engine(localhost_test_url, echo=DEBUG_MODE)
localhost_test_session = sessionmaker(bind=localhost_test_engine)()
localhost_oa_url = f'mysql+mysqlconnector://{quote(USERNAME)}:{quote(PASSWORD)}@{HOST}:{PORT}/coastal-archive?charset=utf8mb4'
localhost_oa_engine = create_engine(localhost_oa_url, echo=DEBUG_MODE)
localhost_oa_session = sessionmaker(bind=localhost_oa_engine)()
ORACLE_NAME = "system"
ORACLE_PASSWORD = "oracle"
ORACLE_IP = "127.0.0.1"
ORACLE_PORT = "15210"
ORACLE_DB = "helloWin"
oracle_url = f"oracle+cx_oracle://{quote(ORACLE_NAME)}:{quote(ORACLE_PASSWORD)}@{ORACLE_IP}:{ORACLE_PORT}/?service_name={ORACLE_DB}"
oracle_engine = create_engine(oracle_url)
time_zone = "%2B10:00"
time_zone_url = f'mysql+mysqlconnector://{quote(USERNAME)}:{quote(PASSWORD)}@{HOST}:{PORT}/test?time_zone={time_zone}'

test_128 = f"""mysql+pymysql://root:{quote("123456")}@172.16.6.128:3306/coastal-system?charset=utf8mb4"""
test_engine_128 = create_engine(test_128, echo=DEBUG_MODE)
test_session_128 = sessionmaker(bind=test_engine_128)()
