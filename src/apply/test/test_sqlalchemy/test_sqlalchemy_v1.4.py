from sqlalchemy import MetaData
from sqlalchemy import create_engine, Column, String, Integer, text, Table, select, delete
from sqlalchemy import insert
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_url

Base = declarative_base()
engine = create_engine(localhost_test_url, echo=True)

metadata_obj = MetaData()
user_table = Table(
    "user_account",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)


class User(Base):
    __tablename__ = 'user_t'
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    username = Column(String(255), index=True, unique=True, nullable=False)


if __name__ == '__main__':
    # todo 函数 outerjoin label aliased alias select_from join_from 右连接
    #  https://docs.sqlalchemy.org/en/14/orm/queryguide.html#controlling-what-to-join-from
    # vos = UserVO.query.outerjoin(
    #     WorkerVO, UserVO.id == WorkerVO.belong
    # ).filter(
    #     and_(UserVO.email.isnot(None), WorkerVO.id.isnot(None))
    # ).distinct().all()
    # print( select(User).where(User.username .is_( None)))

    with engine.connect() as conn:
        # 这个 Row 对象本身的作用类似于Python named tuples .
        result = conn.execute(text("SELECT username FROM user_t"))
        for row in result:
            print(f"username: {row.username}")

    with Session(engine) as session:
        result = session.execute(text("SELECT username FROM user_t"))
        for row in result:
            print(f"username: {row.username}")
    # 建表
    metadata_obj.create_all(engine)
    # Base.metadata.create_all(engine)

    stmt = insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants")
    compiled = stmt.compile()
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

    with engine.connect() as conn:
        result = conn.execute(
            insert(user_table),
            [
                {"name": "sandy", "fullname": "Sandy Cheeks"},
                {"name": "patrick", "fullname": "Patrick Star"}
            ]
        )
        conn.commit()

    stmt = select(User).where(User.name == 'spongebob')
    with Session(engine) as session:
        for row in session.execute(stmt):
            print(row)
    # print(select(user_table.c.name, user_table.c.fullname))

    row = session.execute(select(User)).first()
    # (User(id=1, name='spongebob', fullname='Spongebob Squarepants'),)
    # ORM查询指南  https://www.osgeo.cn/sqlalchemy/orm/queryguide.html

    # 查询 https://www.osgeo.cn/sqlalchemy/tutorial/data_select.html
    # 更新 https://www.osgeo.cn/sqlalchemy/tutorial/data_update.html

    # orm
    session = Session(engine)
    squidward = User(name="squidward", fullname="Squidward Tentacles")
    session.add(squidward)
    session.flush()
    session.commit()
    session.rollback()
    session.close()

    sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()

    patrick = session.get(User, 3)
    session.delete(patrick)
    session.execute(delete(User).where(User.name == "squidward"))
