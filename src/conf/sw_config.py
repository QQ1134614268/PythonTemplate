# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SHENWAN_AUTH_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format('root', "123456", "8.129.48.72", "30894", 'auth')
shenwan_auth_engine = create_engine(SHENWAN_AUTH_URL, echo=True)
shenwan_auth_session = sessionmaker(bind=shenwan_auth_engine)()