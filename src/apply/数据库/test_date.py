# -*- coding:utf-8 -*-
"""
@Time: 2021/8/24
@Description:
"""

from sqlalchemy import Column, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from apply.数据库.test_sql import BaseTable

Base = declarative_base()


class TestDate(BaseTable):
    __tablename__ = "test_date_t"
    date = Column(Date)


def exec_sql(sql):
    response = session.execute(sql)
    try:
        res = [dict(zip(item.keys(), item)) for item in response]
        print(res)
        return res
    except:
        print(response)


if __name__ == '__main__':
    sqlserver_url = 'mysql+mysqlconnector://{}:{}@{}/{}?time_zone={}'.format('root', "123456", "127.0.0.1", 'test',
                                                                             "%2B09:00")
    engine = create_engine(sqlserver_url, echo=True)

    # mydb = mysql.connector.connect(
    #     host="localhost",  # 数据库主机地址
    #     user="yourusername",  # 数据库用户名
    #     passwd="yourpassword"  # 数据库密码
    # )

    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    session.add(TestDate(create_time="2021-12-01 12:00:00", date="2021-12-01"))
    session.commit()
    sql = "show VARIABLES like '%time_zone%';"
    exec_sql(sql)
    # SYSTEM
    sql = "set global time_zone = '+00:00';"
    exec_sql(sql)
    exec_sql("flush privileges;")
    # vos = TestDate.query.all()
    vos = session.query(TestDate).all()
    print()
