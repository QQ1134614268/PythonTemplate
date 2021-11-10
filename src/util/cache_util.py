# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import json
import os


#  TODO 全局的,,根据参数缓存  hash_key 未实现
def file_cache(file_path):
    def decorator(func):
        def wrapper(*args, **kw):
            if os.path.exists(file_path):
                with open(file_path, encoding="utf-8", mode='r') as f:
                    return json.loads(f.readline())
            else:
                res = func(*args, **kw)
                with open(file_path, encoding="utf-8", mode='w') as f:
                    f.write(json.dumps(res))
                return res

        return wrapper

    return decorator


if __name__ == '__main__':
    @file_cache("test.txt")
    def add(d, b):
        return d + b


    print(add(1, 1))
