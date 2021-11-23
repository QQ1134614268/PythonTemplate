# -*- coding:utf-8 -*-
"""
@Time: 2021/8/18
@Description:
"""

import pymssql


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
