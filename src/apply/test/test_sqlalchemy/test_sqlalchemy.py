# -*- coding:utf-8 -*-
"""
@Time: 2021/10/9
@Description:
"""
from unittest import TestCase

from sqlalchemy import Column, String, Integer, create_engine, Boolean, func, desc, FLOAT, DECIMAL, alias
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.db_conf import localhost_test_url, localhost_test_session

Base = declarative_base()


class TestUser(Base):
    # 表名称
    __tablename__ = 'test_user'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(64))
    uid = Column(String(64), unique=True)
    op_mode = Column(Boolean, default=1)
    test_float = Column(FLOAT(precision=10, decimal_return_scale=12), comment="测试float")
    test_float2 = Column(FLOAT(precision='10,2', decimal_return_scale=12), comment="测试float")
    test_decimal = Column(DECIMAL(precision=10, scale=2), comment="测试Decimal")
    # decimal 以字符串存储,存储空间大, 适用价格金额(精度不高,准确度高);
    # float(double) 浮点类型,丢失精度 todo 测试,查看文档


class TestUserInfo(Base):
    # 表名称
    __tablename__ = 'test_user_info'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    user_id = Column(Integer, comment="user_id")
    address = Column(String(64))


class TestSqlalchemy(TestCase):
    engine = create_engine(localhost_test_url, echo=True)
    session = sessionmaker(bind=engine)()

    def test_pre(self):
        Base.metadata.drop_all(self.engine, tables=[TestUser.__table__])
        Base.metadata.create_all(self.engine)

    def test_insert(self):
        localhost_test_session.add(TestUser(id=1, name='tom'))
        # localhost_test_session.add_all([TestUser(id=1, name='tom')])
        # localhost_test_session.query(TestUser).delete()
        # localhost_test_session.query(TestUser).filter(TestUser.id == 1).update({'name': 'name1'})
        localhost_test_session.commit()

    def test_model(self):
        r_data = [{"name": "name", "uid": "uid_1"}, {"name": "name", "uid": "uid_2"}]
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

    def test_select(self):
        res = localhost_test_session.query(TestUser).all()
        print(res)
        res = localhost_test_session.query(TestUser).filter(*[TestUser.id == 1, TestUser.id == 1]).all()
        print(res)
        res = localhost_test_session.query(TestUser).filter(TestUser.id == 1).filter(TestUser.id == 1).all()
        print(res)
        res = localhost_test_session.query(TestUser.id, TestUser.name).filter(TestUser.id.is_(None)).all()
        print(res)
        res = localhost_test_session.query(TestUser).order_by(desc(TestUser.id)).all()
        print(res)
        res = localhost_test_session.query(func.max(TestUser.id), func.min(TestUser.id)).first()
        print(res)
        res = localhost_test_session.query(TestUser).offset(20).limit(10).all()
        print(res)
        res = localhost_test_session.query(func.max(TestUser.id)).scalar()
        print(res)

        # select_from
        res = localhost_test_session.query(TestUser, TestUserInfo).select_from(TestUser) \
            .join(TestUserInfo, TestUserInfo.user_id == TestUser.id).scalar()
        print(res)
        res = localhost_test_session.query(TestUser, TestUserInfo) \
            .join(TestUserInfo, TestUserInfo.user_id == TestUser.id).all()
        print(res)

        # 自连接
        alias1 = alias(TestUser, name="t1")
        alias2 = alias(TestUser, name="t2")
        # 参考: sqlalchemy.sql.Alias
        res = localhost_test_session.query(alias1, alias2).join(alias2, alias1.columns.id == alias2.columns.id).all()
        print(res)
