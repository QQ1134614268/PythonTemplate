# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOST = "42.194.237.10"
PORT = "30003"
PASSWORD = "6HOoIAqc22uw7gc2"

USERNAME = 'root'

DB = "pledge_risk_02"
DEBUG_MODE = False
url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DB)
engine = create_engine(url, echo=DEBUG_MODE)
session = sessionmaker(bind=engine)()


def exec_sql(x_sql2):
    response = session.execute(x_sql2)
    return [dict(zip(item.keys(), item)) for item in response]


def get_tables(db):
    sql = "select table_name from information_schema.tables where table_schema='{}'".format(db)
    tbs = []
    for item in exec_sql(sql):
        tbs.append(item["TABLE_NAME"])
    return tbs


def get_pks(db, tb_name):
    sql = """SELECT
        k.column_name,
        t.table_name,
        k.table_schema 
    FROM
        information_schema.table_constraints t
        JOIN information_schema.key_column_usage k USING ( constraint_name, table_schema, table_name ) 
    WHERE
        t.constraint_type = 'PRIMARY KEY' 
        AND t.table_schema = '{}' 
        AND t.table_name = '{}'""".format(db, tb_name)
    return exec_sql(sql)


def get_cols():
    """
    [
        {
            column_name:xx,
        }
    ]
    """
    sql = """select Column_Name as column_name
            from information_schema.columns where table_schema = '{}' and table_name = '{}' 
            order by ORDINAL_POSITION asc""".format(DB, tb_name)
    return exec_sql(sql)


def get_code_cols():
    ret = []
    cols = get_cols()
    for col_name in cols:
        if "_code" in col_name.lower():
            ret.append(col_name)
    return ret


if __name__ == '__main__':
    sql0 = "select table_name from information_schema.tables where table_schema='{}'".format(DB)
    tables = exec_sql(sql0)

    db_data = {}
    for table_item in tables:
        tb_name = table_item["TABLE_NAME"]
        db_data[tb_name] = {}
        sql = """select Column_Name as column_name
                       from information_schema.columns where table_schema = '{}' and table_name = '{}' 
                       order by ORDINAL_POSITION asc""".format(DB, tb_name)
        res = exec_sql(sql)
        for val in res:
            col_name = val["column_name"]

            if "_code" in col_name.lower():
                try:
                    sql3 = "UPDATE {} SET {}= REPLACE(REPLACE({},'.SZA','.SZ'),'.SHA','.SH')".format(
                        tb_name, col_name, col_name)
                    session.execute(sql3)
                except:
                    sql3 = "SELECT * from {} where {} like '%.SZA' or  {} like '%.SHA';".format(
                        tb_name, col_name, col_name)
                    ret = exec_sql(sql3)

                    for row in ret:
                        row[col_name] = row[col_name].replace(".SZA", ".SZ").replace(".SHA", ".SH")
                        try:
                            # sql = 'UPDATE plan_trial_calculation SET status=:status, end_at=:end_at WHERE id=:id '
                            sql4 = 'UPDATE {} SET {}'.format(
                                tb_name, ', '.join('{}=:{}'.format(k, k) for k, v in row.items()))
                            session.execute(sql4, row)
                        except Exception as e:
                            if "Duplicate entry" in str(e):
                                pass
                            else:
                                print(e)
                                raise e
        del_sql = "delete from {} where {} like '%.SZA' or {} like '%.SHA'".format(tb_name, col_name, col_name)
        session.execute(del_sql)
        session.commit()
