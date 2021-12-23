# -*- coding:utf-8 -*-
"""
@Time: 2021/12/23
@Description:
"""
from threading import Thread
from time import sleep


def async_task(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


if __name__ == '__main__':
    @async_task
    def func_a():
        sleep(2)
        print("函数A睡了2秒钟。。。。。。")


    def func_b():
        print("后调用,先返回了")


    func_a()
    func_b()
