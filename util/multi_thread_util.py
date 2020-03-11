# -*- coding:utf-8 -*-
import json
from threading import Thread

import redis


def create_redis():
    return redis.Redis('127.0.0.1', 6379)


redis_cli = create_redis()


def lock(key, value, ex=60 * 10):
    return redis_cli.set(key, value, nx=True, ex=ex)


def del_key(key):
    redis_cli.delete(key=key)


def get_task_list():
    return redis_cli.lrange("task_list", 0, 100)


def get_task_args():
    return redis_cli.lrange("task_list", 0, 100)


def exec_task(b):
    print(type(b), b)
    # 对一个任务枷锁 锁的参数
    pass


def multi_process(func, args, count):
    task_list = get_task_list()
    for task in task_list:
        value_set = lock(task, "1")
        if value_set == 1:
            arg = redis_cli.get("task_task1")
            arg_dict = json.loads(arg)
            exec_task(arg_dict)
            redis_cli.delete("task1")

    for i in range(count):
        t = Thread(target=func, args=(args,))
        t.start()


if __name__ == '__main__':
    a = exec_task
    b = (1, 2)
    a(b)
