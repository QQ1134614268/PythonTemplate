# -*- coding:utf-8 -*-
"""
@Time: 2021/8/24
@Description:
"""
import os
from unittest import TestCase


class TestSqlacodegen(TestCase):

    def test_sqlacodegen(self):
        db = "test"
        cmd = f"sqlacodegen mysql://root:123456@127.0.0.1:3306/{db}?charset=utf8mb4 > {db}_models.py"
        # cmd = "sqlacodegen mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8mb4 > models.py"

        # cmd = "sqlacodegen oracle+cx_oracle://system:oracle@127.0.0.1:15210/?service_name=helowin > old_models.py"
        # cx_Oracle.init_oracle_client(lib_dir=r"D:\dev\instantclient_21_3")

        os.system(cmd)
