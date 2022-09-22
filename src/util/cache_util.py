# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import json
from datetime import datetime

from conf.config import FILE_FORMAT
from conf.json_config import MyJsonEncoder


# json yaml prop
def to_json_file(file_path="", indent=None):
    """
    存储结果
    :param file_path: 文件名
    :param indent:
    :return:
    """

    # if not file_path:
    #     file_path = datetime.now().strftime(FILE_FORMAT) + ".json"

    def decorator(func):
        def wrapper(*args, **kw):
            res = func(*args, **kw)
            content = json.dumps(res, cls=MyJsonEncoder, ensure_ascii=False, indent=indent)
            with open(file_path + datetime.now().strftime(FILE_FORMAT) + ".json", encoding="utf-8", mode='w') as f:
                f.write(content)
            return res

        return wrapper

    return decorator


if __name__ == '__main__':
    @to_json_file()
    def add():
        return 1


    print(add())
