# -*- coding:utf-8 -*-
"""
@Time: 2021/12/23
@Description:
"""
from multiprocessing import Pool
from threading import Thread
from time import sleep

from config.base_obj import Human


class Env(Human):
    pass


def async_task(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def my_print(x):
    print(x)


# todo - 多进程,线程, 队列, task, demo, spark,kafka, 转文件,读文件, 装饰器,  file-util,
#  任务分配, 函数-- hash
#  资源设置, 系统配置, 内存, io(网络),cpu
#  mapreduce中环境配置-- 图片脚本,非规律参数.
#  异步
#  结果聚合
#  异常处理, 稳定的
#  日志追踪, 每一步结果,缓存数据
#  读写文件, json
#  环境 -- 回滚操作,异常,取消,
#  验证数据完整性, 入参出参
#  定时任务
#  场景: 图片脚本, 数据清洗

#  queue, 幂等, threading async process, @functools.lru_cache

if __name__ == '__main__':
    @async_task
    def func_a():
        sleep(2)
        print("函数A睡了2秒钟。。。。。。")


    def func_b():
        print("后调用,先返回了")


    func_a()
    func_b()

    arr = [1, 2, 3, 4, 5]

    pool = Pool()
    pool.map(my_print, arr)
    pool.join()
    pool.close()
