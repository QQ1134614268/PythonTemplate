# -*- coding:utf-8 -*-
"""
@Time: 2021/8/18
@Description:
"""
from sqlalchemy import create_engine

oracle_name = "system"
password = "oracle"
ip = "127.0.0.1"
port = "15210"
db = "helowin"
# oracle: "db_tns":"127.0.0.1:15210/helowin",
# "user": "system",
# "password": "oracle",

sqlserver_ip = "127.0.0.1"
sqlserver_db = "WindDB"
sqlserver_password = "123456"
sqlserver_user = "sa"

sqlserver_url = 'mssql+pymssql://{}:{}@{}/{}'.format(sqlserver_user, sqlserver_password, sqlserver_ip, sqlserver_db)
sqlserver_engine = create_engine(sqlserver_url)

oracle_url = "oracle+cx_oracle://{}:{}@{}:{}/?service_name={}".format(oracle_name, password, ip, port, db)
oracle_engine = create_engine(oracle_url)