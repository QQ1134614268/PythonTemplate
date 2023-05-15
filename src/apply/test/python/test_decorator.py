# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/2 23:23
"""
import functools
import unittest


# 装饰器

# https://www.jianshu.com/p/30a8e723efdc
# def 装饰 def
# def 装饰 class
# class 装饰 def
# class 装饰 class


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("日志记录")
        result = func(*args, **kwargs)
        return result

    return wrapper


@log
def login():
    pass


class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0  # 记录函数被调用的次数

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


# 装饰器类
class Login(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @functools.wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function


@Counter
def today(name='devin'):
    print('Hello, %s! Today is 208-05-25' % name)  # 被装饰的函数带参数的情况


class TestDecorator(unittest.TestCase):

    @staticmethod
    def test_func(name):
        login()

    @staticmethod
    def test_class(name):
        for i in range(10):
            today()
        print(today.count)  # 10


def logit(logfile='out.log'):
    def logging_decorator(func):
        @functools.wraps(func)
        def wrapped_function(*args, **kwargs):
            print(logfile)
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit(logfile="log.txt")
def myfunc1():
    pass
