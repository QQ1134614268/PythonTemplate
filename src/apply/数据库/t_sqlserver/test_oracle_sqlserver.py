# -*- coding:utf-8 -*-
"""
@Time: 2021/8/18
@Description:
"""

import cx_Oracle
import pymssql

from apply.数据库.t_sqlserver.conf_db2 import oracle_name, password, ip, port, db


def test_oracle():
    # 连接数据库，下面括号里内容根据自己实际情况填写
    cx_Oracle.init_oracle_client(lib_dir=r"D:\dev\instantclient_21_3")
    conn = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(oracle_name, password, ip, port, db))
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual")
    # 使用fetchone()方法获取一条数据
    # data=cursor.fetchone()
    # 获取所有数据
    all_data = cursor.fetchall()
    # 获取部分数据，8条
    # many_data=cursor.fetchmany(8)
    print(all_data)
    conn.close()


def test_sqlserver():
    conn = pymssql.connect(**{
        'server': "127.0.0.1",
        'database': "WindDB",
        'password': '123456',
        'user': 'sa'
    })
    cur = conn.cursor()
    sql = "select 1"
    cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    test_sqlserver()
    test_oracle()
