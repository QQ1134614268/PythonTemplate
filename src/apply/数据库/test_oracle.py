# -*- coding:utf-8 -*-
"""
@Time: 2021/11/23
@Description:
"""
import cx_Oracle

from conf.config import ORACLE_NAME, ORACLE_PASSWORD, ORACLE_IP, ORACLE_PORT, ORACLE_DB


def test_oracle():
    # 连接数据库，下面括号里内容根据自己实际情况填写
    cx_Oracle.init_oracle_client(lib_dir=r"D:\dev\instantclient_21_3")
    conn = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(ORACLE_NAME, ORACLE_PASSWORD, ORACLE_IP, ORACLE_PORT, ORACLE_DB))
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


if __name__ == '__main__':
    test_oracle()
