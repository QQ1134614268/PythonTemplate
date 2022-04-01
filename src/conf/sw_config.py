# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SHENWAN_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format('root', "6HOoIAqc22uw7gc2", "124.70.47.167", "20011", 'pledge_risk_01')
shenwan_engine = create_engine(SHENWAN_URL, echo=True)
shenwan_session = sessionmaker(bind=shenwan_engine)()