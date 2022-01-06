# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import json

from apply.issue.issure1.config import DB, session

from util.database_util import get_tables, get_cols

if __name__ == '__main__':
    ret = []
    del_ret = []
    tables = get_tables(session, DB)
    db_data = {}
    for table_name in tables:
        table_data = {
            "col": [],
            "code_col": [],
            "update_sql": []
        }
        db_data[table_name] = {}
        res = get_cols(session, DB, table_name)
        for col_name in res:
            table_data["col"].append(col_name)
            if "_code" in col_name.lower():
                table_data["code_col"].append(col_name)
                # sql3 = "delete from {} where {} like '%.SZA' or {} like '%.SHA'".format(i, col_name, col_name)
                sql3 = "UPDATE IGNORE {} SET {}= REPLACE(REPLACE({},'SZA','SZ'),'SHA','SH')".format(table_name,
                                                                                                    col_name,
                                                                                                    col_name)
                table_data["update_sql"].append(col_name)
                ret.append(sql3)
                del_ret.append(
                    "delete from {} where {} like '%SZA' or {} like '%SHA' ".format(table_name, col_name, col_name))
    # dict 转 json 输出文件
    with open("out_all.txt", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(db_data))
    # dict 转 json 输出文件
    with open("out.txt", mode="w", encoding="utf-8") as f:
        f.write(";\n".join(ret))
    # dict 转 json 输出文件
    with open("del_out.txt", mode="w", encoding="utf-8") as f:
        f.write(";\n".join(del_ret))
