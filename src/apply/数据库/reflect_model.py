# -*- coding:utf-8 -*-
"""
@Time: 2021/8/24
@Description:
"""
import os

cmd = "sqlacodegen mysql://root:123456@127.0.0.1:3306/test?charset=utf8mb4 > old_models.py"
# cmd = "sqlacodegen mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8mb4 > models.py"

# cmd = "sqlacodegen oracle+cx_oracle://system:oracle@127.0.0.1:15210/?service_name=helowin > old_models.py"
# cx_Oracle.init_oracle_client(lib_dir=r"D:\dev\instantclient_21_3")


os.system(cmd)
