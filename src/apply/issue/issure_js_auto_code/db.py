from sqlalchemy import Column, String, Integer, create_engine, Boolean
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from conf.config import localhost_test_url

from datetime import datetime
from unittest import TestCase

from sqlalchemy import Column, create_engine, DateTime, Integer, TIMESTAMP, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import func

from conf.config import time_zone_url

Base = declarative_base()


class Table:
    table_schema = Column(String)
    table_name = Column(String)
    table_comment = Column(String)
    column_name = Column(String)
    column_type = Column(String)
    column_comment = Column(String)
    data_type = Column(String)


class DbUtil:
    def __init__(self, username, password, host, port, db):
        url = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(username, password, host, port, db)
        self.engine = create_engine(url, echo=True)
        # self.session = sessionmaker(bind=self.engine)()

    def exec(self, sql, args=None):
        response = self.engine.execute(sql, args)
        res = [dict(zip(item.keys(), item)) for item in response]
        return res


class TestDb(TestCase):

    def test_run(self):
        sql = "select * from user where user_name=:name and id=:id"
        url = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format("root", "123456", "127.0.0.1", "3306", "oa")
        engine = create_engine(url, echo=True)
        session = sessionmaker(bind=engine)()
        res = session.execute(sql, {"id": 1, "name": "test"})
        result2 = res.fetchall()  # 获取全部
        print(result2)

    def test_run_all(self):
        sql = "select * from user where user_name=%(name)s and id=%(id)s"
        url = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format("root", "123456", "127.0.0.1", "3306", "oa")
        engine = create_engine(url, echo=True)
        res = engine.execute(sql, {"id": 1, "name": "test"})
        result2 = res.fetchall()  # 获取全部
        print(result2)
