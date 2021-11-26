# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/2 23:23
"""
import functools

import time


# todo

# https://www.jianshu.com/p/30a8e723efdc
# @functools.wraps
# @classmethod、@staticmethod
# @property -> getter/setter方法
# 4).装饰函数 -> 装饰类

def Length(cls):
    class NewClass(cls):
        @property
        def length(self):
            if hasattr(self, '__len__'):
                self._length = len(self)
            return self._length

        @length.setter
        def length(self, value):
            self._length = value

    return NewClass


# 4).装饰函数 -> 装饰类
@Length
class Tool(object):
    pass


t = Tool()
t.length = 10
print(t.length)  # 10


# @functools.wraps
def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time() - start)
        return result

    return wrapper


@timethis
def countdown(n: int):
    """Counts down"""
    while n > 0:
        n -= 1


countdown(10000000)  # 1.3556335
print(countdown.__name__, ' doc: ', countdown.__doc__, ' annotations: ', countdown.__annotations__)


# @classmethod、@staticmethod
class A(object):
    @classmethod
    def method(cls):
        pass


# @property -> getter/setter方法
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


s = Student()
s.core = 60
print('s.score = ', s.score)
s.score = 999  # ValueError: score must between 0~100!
