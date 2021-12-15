# -*- coding:utf-8 -*-
"""
@Time: 2021/7/30
@Description:
"""
import re
import unittest

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from util.my_util import Data

Base = declarative_base()


class RightManage(Base):
    __table_name__ = "right_manage"
    pass


class Filed:
    def __init__(self, Field, Type, Collation, Null, Default, Extra, Privilege, Key, Comment):
        self.Field = Field
        self.Type = Type
        self.Collation = Collation
        self.Null = Null
        self.Key = Key
        self.Default = Default
        self.Extra = Extra
        self.Privilege = Privilege
        self.Key = Key
        self.Comment = Comment


class TestMysql(unittest.TestCase):

    def setUp(self):
        # 创建对象的基类:
        # 初始化数据库连接:
        dev = "mysql+pymysql://root:123456@127.0.0.1:3306/pledge_risk_01?charset=utf8"
        self.engine = create_engine(dev, echo=True)
        self.session = sessionmaker(bind=self.engine)()
        self.session.execute("select 1")  # 跳过session初始化的一些条件查询,便于后续debug

    def test_table_dic(self):
        ret = self.session.execute("show full fields from {}".format(RightManage.__tablename__))
        data = {}
        for it in ret:
            vo = Filed(*it)
            data[vo.Field] = self.get_data(vo.Type)
        print(str(data).replace("'", '"'))

    def get_data2(self, f_type):
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
