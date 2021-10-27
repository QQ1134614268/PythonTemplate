# -*- coding:utf-8 -*-
"""
@Time: 2021/8/17
@Description:
"""

import os

import pymssql

from util.log_util import logger


def get_file(path):
    files = os.listdir(path)
    ret = []
    for file in files:
        f_path = os.path.join(path, file)
        if os.path.isfile(f_path):
            ret.append(f_path)
    return ret


def run():
    cxn = pymssql.connect(**{'server': "127.0.0.1", 'database': "WindDB", 'password': '123456', 'user': 'sa'})
    cur = cxn.cursor()
    # file_dir = r'D:\桌面文件夹\万得和巨潮表数据SQL'
    # file_list = get_file(file_dir)
    file_list = [r"D:\桌面文件夹\dbo.CBONDPRICES.Table.sql"]
    row = 0
    for file in file_list:
        sql = ""
        with open(file, encoding="utf-16") as f:
            for line in f:
                row += 1
                if line.startswith("GO"):
                    continue
                if line.startswith("INSERT"):
                    try:
                        cur.execute(sql)
                        print(row)
                    except:
                        logger.exception("异常")
                    sql = line
                else:
                    sql += line
            else:
                with open("result.txt", mode="w+", encoding="utf-8") as f2:
                    f2.write(file)
        cxn.commit()
    cxn.close()


if __name__ == '__main__':
    run()
