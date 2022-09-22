# -*- coding:utf-8 -*-
"""
@Time: 2021/10/9
@Description:
"""
from unittest import TestCase

from sqlalchemy import Column, String, Integer, create_engine, Boolean
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from conf.db_conf import localhost_test_url

Base = declarative_base()


class TestUser(Base):
    # 表名称
    __tablename__ = 'test_user'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(64))
    uid = Column(String(64), unique=True)
    op_mode = Column(Boolean, default=1)


class TestSqlalchemy(TestCase):
    engine = create_engine(localhost_test_url, echo=True)
    session = sessionmaker(bind=engine)()

    def test_model(self):
        # Base.metadata.drop_all(engine)
        # Base.metadata.create_all(engine)
        r_data = [{"name": "name", "uid": "address"}, {"name": "name", "uid": "address"}]
        insert_stmt = insert(TestUser).values(r_data)
        on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
            name=insert_stmt.inserted.name,
            address=insert_stmt.inserted.uid,
        )
        self.session.execute(on_duplicate_key_stmt)
        self.session.commit()

    def test_session_name_arg(self):
        sql = "select * from test_user where name=:name and id=:id"
        res = self.session.execute(sql, {"id": 1, "name": "test"})
        result2 = res.fetchall()  # 获取全部
        print(result2)

    def test_engine_name_arg(self):
        sql = "select * from test_user where name=%(name)s and id=%(id)s"
        res = self.engine.execute(sql, {"id": 1, "name": "test"})
        result2 = res.fetchall()  # 获取全部
        print(result2)
