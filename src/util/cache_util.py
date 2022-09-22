# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import json
from datetime import datetime

import time

from conf.config import FILE_FORMAT
from conf.json_config import MyJsonEncoder


# json yaml prop
def to_json_file(file_path="result.json", time_flag=True, indent=None):
    """
    存储结果
    :param time_flag:
    :param file_path: 文件名
    :param indent:
    :return:
    """

    def decorator(func):
        def wrapper(*args, **kw):
            res = func(*args, **kw)
            if time_flag:
                path = get_new_file_name(file_path)
            else:
                path = file_path
            with open(path, encoding="utf-8", mode='w') as f:
                f.write(json.dumps(res, cls=MyJsonEncoder, ensure_ascii=False, indent=indent))
            return res

        return wrapper

    return decorator


def get_new_file_name(file_name=""):
    if "." in file_name:
        name = file_name[0:file_name.rindex(".")]
        suffix = file_name[file_name.rindex("."):]
        return f"{name}_{datetime.now().strftime(FILE_FORMAT)}{suffix}"
    return f"{file_name}_{datetime.now().strftime(FILE_FORMAT)}.json"


if __name__ == '__main__':
    @to_json_file()
    def add():
        return 1


    @to_json_file()
    def add2():
        return 1


    @to_json_file()
    def add3():
        return 1


    print(add())
    time.sleep(2)
    print(add())
    print(get_new_file_name())
    print(get_new_file_name("da.txt"))
