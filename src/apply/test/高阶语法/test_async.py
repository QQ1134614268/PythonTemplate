# -*- coding:utf-8 -*-
"""
@Time: 2021/12/23
@Description:
"""

import asyncio
import unittest
from time import sleep

from util.time_util import get_now_str
# asyncio.run 运行一个异步函数
# asyncio.gather 运行多个异步函数
# 采用函数gather


async def test_a():
    print("标 1", get_now_str())
    sleep(2)
    print("标 2", get_now_str())


class TestAsync(unittest.TestCase):

    def test_no_await(self):
        test_a()  # 不会执行
        test_a()

    async def test_await(self):
        await test_a()  # 不会执行 需要 asyncio.run(test_await())
        await test_a()

    def test_run(self):
        asyncio.run(test_a())

    def test_await_task(self):
        task = asyncio.create_task(test_a())
        # await task # SyntaxError: 'await' outside async function
        #  异常        await只能用在 async函数中, asyncio.run(test_await_task())

        # await asyncio.wait(tasks)

    def test_loop_task(self):
        # 异步
        loop = asyncio.get_event_loop()
        tasks = [test_a() for i in range(5)]
        loop.run_until_complete(asyncio.wait(tasks))
