# -*- coding:utf-8 -*-
"""
@Time: 2021/7/22
@Description:
"""
import sys


def test_get_func_name():
    print(sys._getframe().f_code.co_name)


def my_func():
    lis = []
    res = lis + ['get', 'func', 'vars']
    print(res)
    words = "Life is short, You need Python!"
    print(words)


def get_func_var_names(func):
    func_vars = func.__code__.co_varnames
    print(func_vars)


if __name__ == "__main__":
    test_get_func_name()
    get_func_var_names(my_func)
