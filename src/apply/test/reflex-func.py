# -*- coding:utf-8 -*-
"""
@Time: 2021/7/22
@Description:
"""
import sys


def a():
    print(sys._getframe().f_code.co_name)


def my_func():
    lis = []
    dic = dict()
    res = lis + ['get', 'func', 'vars']
    words = "Life is short, You need Python!"
    print(words)


def get_func_varnames(func):
    func_vars = func.__code__.co_varnames
    print(func_vars)


if __name__ == "__main__":
    a()
    get_func_varnames(my_func)
