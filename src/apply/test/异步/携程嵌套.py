# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/2 23:20
"""

import asyncio


async def foo():
    print('----start foo')
    await asyncio.sleep(3)
    print('----end foo')


async def bar():
    print('****start bar')
    await asyncio.sleep(2)
    print('****end bar')


async def foos():
    print('----------------------')
    tasks = []
    for i in range(3):
        tasks.append(asyncio.create_task(foo()))
    await asyncio.wait(tasks)
    print('----88----')


async def main():
    tasks = []
    for i in range(3):
        tasks.append(asyncio.create_task(foos()))
    for j in range(3):
        tasks.append(asyncio.create_task(bar()))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
