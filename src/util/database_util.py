# -*- coding:utf-8 -*-
"""
@Time: 2021/11/19
@Description:
"""
import unittest

from conf.db_conf import DB, localhost_test_session

def exec_sql(curr_session, sql):
    result = curr_session.execute(sql)
    return res_to_dic(result)


def exec_to_list_dict(curr_session, sql, paras=None):
    result = curr_session.execute(sql, paras)
    return res_to_dic(result)


def exec_to_list(curr_session, sql, params=None):
    result = curr_session.execute(sql, params)
    return res_to_list(result)


def res_to_dic(result):
    return [dict(zip(item.keys(), item)) for item in result]


def res_to_list(result):
    return [item[0] for item in result]


def get_tables(curr_session, db):
    sql = "select table_name as table_name from information_schema.tables where table_schema=:table_schema"
    return exec_to_list(curr_session, sql, {"table_schema": db})


def get_cols(curr_session, db, tb_name):
    sql = """select Column_Name as column_name
            from information_schema.columns where table_schema = :table_schema and table_name = :table_name 
            order by ORDINAL_POSITION """
    return exec_to_list(curr_session, sql, {"table_schema": db, "table_name": tb_name})


def get_unique_cols(curr_session, db, tb_name):
    sql = """SELECT
        k.column_name as column_name,
        t.table_name,
        k.table_schema 
    FROM
        information_schema.table_constraints t
        JOIN information_schema.key_column_usage k USING ( constraint_name, table_schema, table_name ) 
    WHERE
        (t.constraint_type = 'PRIMARY KEY' or t.constraint_type = 'UNIQUE')
        AND t.table_schema = :table_schema 
        AND t.table_name = :table_name """
    res = curr_session.execute(sql, {"table_schema": db, "table_name": tb_name})
    return [item["column_name"] for item in res_to_dic(res)]


class Test(unittest.TestCase):
    def test_get_tables(self):
        print(get_tables(localhost_test_session, DB))

    def test_get_cols(self):
        print(get_cols(localhost_test_session, DB, 'dividend_bond'))

    def test_get_pks(self):
        print(get_unique_cols(localhost_test_session, DB, 'dividend_bond'))

    def test_version(self):
        sql = "select version()"
        print(exec_to_list_dict(localhost_test_session, sql))
