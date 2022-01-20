# -*- coding:utf-8 -*-
"""
@Time: 2021/11/9
@Description:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOST = "42.194.237.10"
PORT = "30003"
PASSWORD = "6HOoIAqc22uw7gc2"
USERNAME = 'root'
gj_DB = "pledge_risk_02"
DEBUG_MODE = False
gj_url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, gj_DB)
gj_engine = create_engine(gj_url, echo=DEBUG_MODE)
gj_session = sessionmaker(bind=gj_engine)()
