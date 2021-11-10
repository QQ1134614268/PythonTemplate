# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from util.cache_util import file_cache
from util.log_util import logger

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


@file_cache("tables.json")
def get_tables(db=DB):
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
        (t.constraint_type = 'PRIMARY KEY' or t.constraint_type = 'UNIQUE')
        AND t.table_schema = '{}' 
        AND t.table_name = '{}'""".format(db, tb_name)
    return [item["COLUMN_NAME"] for item in exec_sql(sql)]


def get_cols(db, tb_name):
    """
    [
        {
            COLUMN_NAME:xx,
        }
    ]
    """
    sql = """select Column_Name as COLUMN_NAME
            from information_schema.columns where table_schema = '{}' and table_name = '{}' 
            order by ORDINAL_POSITION """.format(db, tb_name)
    return [item["COLUMN_NAME"] for item in exec_sql(sql)]


def get_code_cols(db, tb_name):
    ret = []
    cols = get_cols(db, tb_name)
    for col_name in cols:
        if "_code" in col_name.lower():
            ret.append(col_name)
    return ret


def get_select_cols(db, tb_name):
    return get_code_cols(db, tb_name) + get_pks(db, tb_name)


def get_pks_data(db, tb_name):
    pks = get_pks(db, tb_name)
    sql = "select {} from {}".format(", ".join(pks), tb_name)
    return exec_sql(sql)

    # return list(tuple(((item[pk] for pk in pks), for item in data)))
    # return list(session.execute(sql))


def get_col_data(db, tb_name):
    all_cols = get_select_cols(db, tb_name)
    code_cols = get_code_cols(db, tb_name)
    #  todo 优化 all_cols 少量数据
    sql = "select {} from {} where {}".format(
        ", ".join(all_cols), tb_name, " or ".join(
            ["{} like '%.SZA' or  {} like '%.SHA'".format(col, col) for col in code_cols]
        ) or '1=1'
    )
    all_data = exec_sql(sql)
    pks_data = get_pks_data(db, tb_name)

    ret = []
    pks = get_pks(db, tb_name)
    for data in all_data:
        old_pk = {pk: data[pk] for pk in pks}
        for col_name in code_cols:
            data[col_name] = data[col_name].replace(".SZA", ".SZ").replace(".SHA", ".SH")

        key_new = {pk: data[pk] for pk in pks}

        pks_data.remove(old_pk)
        if key_new in pks_data:
            # return [dict(zip(item.keys(), item)) for item in response]
            ret.append(key_new)
    return ret


def remove_dumplicate(db, tb_name):
    remove_keys = get_col_data(db, tb_name)
    if remove_keys:
        sql = "delete from {} where {}".format(
            tb_name,
            " or ".join(["{}=:{}".format(key, key) for key in remove_keys[0].keys()])
            # ', '.join('{}=:{}'.format(k, k) for k, v in row.items()
        )
        session.execute(sql, remove_keys)


@file_cache("big_table.json")
def big_table():
    tables = get_tables(DB)
    # tables = ["guarantee_bonds"]
    ret = []
    for tb_name in tables:
        sql = "select count(1) from {}".format(tb_name)
        res = session.execute(sql)
        for i in res:
            if i[0] > 100000:
                ret.append(tb_name)
    logger.info("跳过的表:", ",".join(ret))
    return ret


@file_cache("update_sql.json")
def mysql_sc(table_name):
    ret = []
    with open("out.txt", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if table_name in line:
                try:
                    logger.info("update sql", line)
                    session.execute(line.replace("\n", ""))
                    session.commit()
                except Exception as e:
                    ret.append(table_name)
                    logger.error("sql异常", repr(e))
    logger.info("update异常表", ", ".join(ret))
    return ret


def main():
    logger.info("--------------脚本开始-------------------")
    # mysql_sc()
    tables = get_tables(DB)
    tables = ["guarantee_bonds"]
    bt = big_table()
    c = ["sec_config"]

    for table_name in tables:
        logger.info("进度", table_name)
        # if table_name in bt:
        #     continue
        if table_name in c:
            continue
        if not get_pks(DB, table_name):
            logger.warning("no pk", table_name)
            continue
        remove_dumplicate(DB, table_name)
        session.commit()
        mysql_sc(table_name)

    logger.info("--------------脚本结束-------------------")


if __name__ == '__main__':
    main()
