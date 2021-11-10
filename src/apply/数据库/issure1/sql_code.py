# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def exec_sql(sql2):
    response = session.execute(sql2)
    return [dict(zip(item.keys(), item)) for item in response]

HOST = "42.194.237.10"
PORT = "30003"
PASSWORD = "6HOoIAqc22uw7gc2"

USERNAME = 'root'

DB = "pledge_risk_02"
DEBUG_MODE = False
url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DB)
engine = create_engine(url, echo=DEBUG_MODE)
session = sessionmaker(bind=engine)()


tables = []
ret = []
del_ret = []
if __name__ == '__main__':

    res = session.execute("select table_name from information_schema.tables where table_schema='{}'".format(DB))
    for i in res:
        tables.append(i[0])

    sql = """select Column_Name as column_name
                from information_schema.columns where table_schema = '{}' and table_name = '{}' 
                order by ORDINAL_POSITION asc"""
    db_data = {}

    for i in tables:
        if i=="securities_group":
            print()
        table_data = {
            "col": [],
            "code_col": [],
            "update_sql": []
        }
        db_data[i] = {}
        sql2 = sql.format(DB, i)
        res = exec_sql(sql2)
        for val in res:
            col_name = val["column_name"]
            table_data["col"].append(col_name)
            if "_code" in col_name.lower():
                table_data["code_col"].append(col_name)
                # sql3 = "delete from {} where {} like '%.SZA' or {} like '%.SHA'".format(i, col_name, col_name)
                sql3 = "UPDATE IGNORE {} SET {}= REPLACE(REPLACE({},'.SZA','.SZ'),'.SHA','.SH')".format(i, col_name,
                                                                                                        col_name)
                table_data["update_sql"].append(col_name)
                ret.append(sql3)
                del_ret.append("delete from {} where {} like '%.SZA' or {} like '%.SHA' ".format(i, col_name, col_name))
    # dict 转 json 输出文件
    with open("out_all.txt", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(db_data))
    # dict 转 json 输出文件
    with open("out.txt", mode="w", encoding="utf-8") as f:
        f.write(";\n".join(ret))
    # dict 转 json 输出文件
    with open("del_out.txt", mode="w", encoding="utf-8") as f:
        f.write(";\n".join(del_ret))
