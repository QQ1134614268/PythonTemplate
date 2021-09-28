# -*- coding:utf-8 -*-
"""
@Time: 2021/8/18
@Description:
"""
from sqlalchemy import create_engine

from src.apply.数据库.t_sqlserver.conf_db2 import oracle_name, password, ip, port, db
from src.apply.数据库.t_sqlserver.conf_db2 import sqlserver_ip, sqlserver_user, sqlserver_password, sqlserver_db

sqlserver_url = 'mssql+pymssql://{}:{}@{}/{}'.format(sqlserver_user, sqlserver_password, sqlserver_ip, sqlserver_db)
oracle_engine = create_engine(sqlserver_url)

oracle_url = "oracle+cx_oracle://{}:{}@{}:{}/?service_name={}".format(oracle_name, password, ip, port, db)
oracle_engine = create_engine(oracle_url)
