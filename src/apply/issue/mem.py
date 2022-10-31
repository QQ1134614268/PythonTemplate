# -*- coding:utf-8 -*-
"""
@Time: 2022/10/25
@Description:
"""

import json
from unittest import TestCase


# 获取进程 ps -ef | grep {cmd}
# 内存相关:
# cat /proc/12375/smaps
# cat /proc/24546/status
# cat /proc/meminfo
# cat /proc/9776/maps

# 获取线程堆栈
#     子进程
#     获取线程
#  方法栈


def exec_cmd():
    pass


def get_proc():
    #
    cmd = ""
    cmd = f"ps -ef | grep {cmd}"

    pass


class TestAutoCode(TestCase):
    def test_run(self):
        with open("指标.txt", encoding="utf-8", mode='r') as f:
            for line in f.readlines():
                menu_list = json.loads(line)
                print(menu_list)
