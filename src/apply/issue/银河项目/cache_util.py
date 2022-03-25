# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import json
import os

import time


def to_file(file_path='out.json', unique=False, load=False, skip_err=False):
    """
    存储结果
    :param file_path: 文件名
    :param unique: 每次生成新文件
    :param load: unique=false, 从文件加载
    :param skip_err:
    :return:
    """

    def decorator(func):
        def wrapper(*args, **kw):
            if os.path.exists(file_path) and load:
                with open(file_path, encoding="utf-8", mode='r') as f:
                    return json.loads(f.readline())
            else:
                res = func(*args, **kw)
                if unique:
                    path = file_path + str(time.time())
                else:
                    path = file_path
                try:
                    write_file(res, path)
                except Exception as e:
                    if not skip_err:
                        raise e
                    print(e)
                return res

        return wrapper

    return decorator


def list_to_file(file_path='out.json'):
    def decorator(func):
        def wrapper(*args, **kw):
            res = func(*args, **kw)
            assert isinstance(res, list), "导出到文件异常,结果不是list"
            text = "\n".join(res)
            with open(file_path, encoding="utf-8", mode='w') as f:
                f.write(text)
            return res

        return wrapper

    return decorator


def write_file(arg, file_path):
    if isinstance(arg, list):
        cont = "\n".join(arg)
    if isinstance(arg, dict):
        cont = json.dumps(arg)
    if isinstance(arg, str):
        cont = arg
    with open(file_path, encoding="utf-8", mode='w') as f:
        f.write(cont)


if __name__ == '__main__':
    @to_file("test.txt")
    def add(d, b):
        return d + b


    print(add(1, 1))
