# -*- coding:utf-8 -*-
"""
@Time: 2021/8/24
@Description:
"""
from datetime import datetime
from unittest import TestCase

from sqlalchemy import Column, create_engine, DateTime, Integer, TIMESTAMP, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import func

from conf.db_conf import time_zone_url

Base = declarative_base()


class BaseTable(Base):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    # create_user =  Column( Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)
    # update_user =  Column( Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)


class TestDate(BaseTable):
    __tablename__ = "test_date_t"
    date = Column(DateTime)
    time = Column(DateTime)
    date_time = Column(DateTime)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp(), server_onupdate=func.current_timestamp(),
                       onupdate=func.current_timestamp())
    date_time_str = Column(String)


def exec_sql(sql):
    response = session.execute(sql)
    try:
        res = [dict(zip(item.keys(), item)) for item in response]
        print(res)
        return res
    except:
        print(response)


class TestMysql(TestCase):
    def setUp(self):
        engine = create_engine(time_zone_url, echo=True)
        # Base.metadata.drop_all(engine)
        # Base.metadata.create_all(engine)
        global session;
        session = sessionmaker(bind=engine)()
        # exec_sql("show VARIABLES like '%time_zone%'; ")
        # exec_sql("set time_zone = '+03:00';")
        # exec_sql("show VARIABLES like '%time_zone%'; ")

    def test_a(self):
        # 服务器时区 GTM+8 本机 GTM+8 url GTM+8

        # now() sysdate()

        # mysql 默认 SYSTEM

        new_time = datetime(2021, 1, 1, 12, 00, 00)
        session.add(
            TestDate(
                date=datetime.now(),
                time=datetime.now(),
                datetime=datetime.now(),
                date_time_str="2000-01-01 00:00:00",
            )
        )
        session.commit()
        # sql2 = "set time_zone = '+12:00';"
        # exec_sql(sql2)

        vos = session.query(TestDate).all()
        print()
