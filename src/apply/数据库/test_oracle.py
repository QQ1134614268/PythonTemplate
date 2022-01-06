# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""

# 获取表名、表注释
import cx_Oracle

from conf.oracle_config import oracle_name, password, ip, port, db


class OracleTable:
    def __init__(self, name, password, ip, port, db, table_name=None, target_table_name=None):
        cx_Oracle.init_oracle_client(lib_dir=r"D:\dev\instantclient_21_3")
        conn = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(name, password, ip, port, db))
        # 使用cursor()方法获取操作游标
        self.cursor = conn.cursor()
        # 使用execute方法执行SQL语句
        self.sql_col_template = "select COLUMN_NAME  from user_tab_columns where Table_Name='{}' "
        self.table_name = table_name
        self.data = []
        self.target_table_name = target_table_name

    def get_col(self, table_name=None):
        sql = self.sql_col_template.format(table_name or self.table_name)
        result = self.cursor.execute(sql)
        all_data = self.cursor.fetchall()
        res = []
        for i in all_data:
            res.append(i[0])
        self.data = res

        # 查询字段
        # desc = [d[0] for d in curs.description]
        # result = [dict(zip(desc, line)) for line in curs]
        # curs.close()

        # 参数
        # cursor.bindnames()

    def write_file(self):
        self.get_col()
        with open("origin.txt") as f:
            lines = f.readlines()
            template = "".join(lines)
            arg_sql = "select {} from {}".format(",".join(self.data), self.table_name)
            arg_col = '",\n                       "'.join(self.data)
            template = template.replace(
                "arg_sql", arg_sql
            ).replace(
                "arg_col", arg_col
            ).replace(
                "arg_target_table_name", self.target_table_name
            )
            with open(self.table_name + ".txt", mode="w", encoding="utf-8") as f2:
                f2.write(template)


if __name__ == '__main__':
    ins = OracleTable(oracle_name, password, ip, port, db, "ASHAREIPO", "mysql_ASHAREIPO")
    ins.write_file()
