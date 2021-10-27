# -*- coding:utf-8 -*-
"""
@Time: 2021/10/9
@Description:
"""
from sqlalchemy.dialects.mysql import insert

from sqlalchemy import Column, String, Integer, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class TestUser(Base):
    # 表名称
    __tablename__ = 'test_user'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String(64))
    uid = Column(String(64), unique=True)
    op_mode = Column(Boolean, default=1)


if __name__ == '__main__':
    url = 'mysql+pymysql://{}:{}@{}/{}'.format('root', "123456", "127.0.0.1", 'test')
    engine = create_engine(url, echo=True)
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    vo = TestUser(name="name", uid="address")
    vo2 = TestUser(name="name", uid="address")
    r_data = [vo, vo2]

    insert_stmt = insert(TestUser).values(r_data)
    on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        name=insert_stmt.inserted.name,
        address=insert_stmt.inserted.uid,
    )
    session.execute(on_duplicate_key_stmt)
    session.commit()
