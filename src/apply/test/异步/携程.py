# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/2 23:20
"""
# https://www.cnblogs.com/btxlc/p/10792477.html
# 1.采用函数gather
# 第二种方法 创建task

# asyncio.run 运行一个异步函数
# asyncio.gather 运行多个异步函数
# 采用函数gather

import asyncio


async def foo():
    print('----start foo')
    await asyncio.sleep(1)
    print('----end foo')


async def bar():
    print('****start bar')
    await asyncio.sleep(2)
    print('****end bar')


async def test1():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(foo()))
    for j in range(10):
        tasks.append(asyncio.create_task(bar()))
    await asyncio.wait(tasks)


async def test2():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())
    await task1  # 没有await 不会等待异步执行完
    await task2


async def test3():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(foo()))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(test1())
    # asyncio.run(test2())
    # asyncio.run(test3())
