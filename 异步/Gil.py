# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/2 22:32
"""
import threading
import time


def test():
    print(1, " -- ", time.localtime())
    time.sleep(5)  # 模拟阻塞任务
    print(2, " -- ", time.localtime())


threading.Thread(target=test).start()
print(3, " -- ", time.localtime())
