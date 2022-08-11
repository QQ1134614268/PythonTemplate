# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import json
import logging
from datetime import datetime

from conf.config import FILE_FORMAT
from conf.json_config import MyJsonEncoder


# json yaml prop
def to_json_file(file_path=None, skip_err=False):
    """
    存储结果
    :param file_path: 文件名
    :param skip_err:
    :return:
    """

    if not file_path:
        file_path = datetime.now().strftime(FILE_FORMAT) + ".json"

    def decorator(func):
        def wrapper(*args, **kw):
            res = func(*args, **kw)
            try:
                try:
                    content = json.dumps(res, cls=MyJsonEncoder, ensure_ascii=False)
                except Exception as e:
                    # todo
                    content = "转json异常"
                    logging.warning(content)
                    raise e
                with open(file_path, encoding="utf-8", mode='w') as f:
                    f.write(content)
            except Exception as e:
                if not skip_err:
                    raise e
                logging.exception(e)
            return res

        return wrapper

    return decorator


if __name__ == '__main__':
    # todo 返回数据 dict 对象 list 标量
    @to_json_file()
    def add():
        return 1


    print(add())
