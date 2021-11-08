# -*- coding:utf-8 -*-
"""
@Time: 2021/8/24
@Description:
"""
import os

# cmd = "sqlacodegen mysql://root:123456@8.129.48.72:30894/wind?charset=utf8 > models.py"

# cmd = "sqlacodegen mysql://root:6HOoIAqc22uw7gc2@119.3.178.32:31862/pledge_risk_01?charset=utf8 > risk_models.py"
cmd = "sqlacodegen mysql://root:123456@127.0.0.1:3306/test?charset=utf8 > old_models.py"
# cmd = "sqlacodegen mysql+pymysql://root:123456@127.0.0.1:3306/database or table>models.py"
# cmd = "sqlacodegen oracle+cx_oracle://system:oracle@127.0.0.1:15210/?service_name=helowin > old_models.py"
# cx_Oracle.init_oracle_client(lib_dir=r"D:\dev\instantclient_21_3")
os.system(cmd)
# dict((column.name, getattr(model, column.name)) for column in model.__table__.columns)
