# -*- coding:utf-8 -*-
"""
@Time: 2021/7/30
@Description:
"""
import re
import unittest

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from config.db_conf import localhost_test_url
from util.my_util import Data

Base = declarative_base()


class RightManage(Base):
    __tablename__ = "right_manage"
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")


class Filed:
    def __init__(self, field, type, collation, null, default, extra, privilege, key, comment):
        self.field = field
        self.type = type
        self.collation = collation
        self.null = null
        self.key = key
        self.default = default
        self.extra = extra
        self.privilege = privilege
        self.key = key
        self.comment = comment


class TestReflexTable(unittest.TestCase):

    def setUp(self):
        # 创建对象的基类:
        # 初始化数据库连接:
        self.engine = create_engine(localhost_test_url, echo=True)
        self.session = sessionmaker(bind=self.engine)()
        self.session.execute("select 1")  # 跳过session初始化的一些条件查询,便于后续debug

    def test_table_dic(self):
        ret = self.session.execute("show full fields from {}".format(RightManage.__tablename__))
        data = {}
        for it in ret:
            vo = Filed(*it)
            data[vo.field] = self.get_data(vo.type)
        print(str(data).replace("'", '"'))

    @staticmethod
    def get_data(f_type):
        all_list = re.findall(r"\d+", f_type)
        length = 4
        if all_list:
            length = int(all_list[0])
        return Data.get_data(f_type, length)

    def tearDown(self):
        ...
        # self.session.commit()


if __name__ == '__main__':
    unittest.main()
