# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""

from apply.issue.issure1 import DB, session
from util.cache_util import to_file
from util.database_util import exec_sql, get_tables, get_unique_cols, get_cols
from util.log_util import logger


def get_code_cols(db, tb_name):
    ret = []
    cols = get_cols(db, tb_name)
    for col_name in cols:
        if "_code" in col_name.lower():
            ret.append(col_name)
    return ret


def get_select_cols(db, tb_name):
    return get_code_cols(db, tb_name) + get_unique_cols(db, tb_name)


def get_pks_data(db, tb_name):
    pks = get_unique_cols(db, tb_name)
    sql = "select {} from {}".format(", ".join(pks), tb_name)
    return exec_sql(sql)

    # return list(tuple(((item[pk] for pk in pks), for item in data)))
    # return list(session.execute(sql))


def get_col_data(db, tb_name):
    all_cols = get_select_cols(db, tb_name)
    code_cols = get_code_cols(db, tb_name)
    sql = "select {} from {} where {}".format(
        ", ".join(all_cols), tb_name, " or ".join(
            ["{} like '%.SZA' or  {} like '%.SHA'".format(col, col) for col in code_cols]
        ) or '1=1'
    )
    all_data = exec_sql(sql)
    pks_data = get_pks_data(db, tb_name)

    ret = []
    pks = get_unique_cols(db, tb_name)
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


@to_file("big_table.json")
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


@to_file("update_sql.json")
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
    # tables = ["guarantee_bonds"]
    bt = big_table()
    c = ["sec_config"]

    for table_name in tables:
        logger.info("进度", table_name)
        # if table_name in bt:
        #     continue
        if table_name in c:
            continue
        if not get_unique_cols(DB, table_name):
            logger.warning("no pk", table_name)
            continue
        remove_dumplicate(DB, table_name)
        session.commit()
        mysql_sc(table_name)

    logger.info("--------------脚本结束-------------------")


if __name__ == '__main__':
    main()
