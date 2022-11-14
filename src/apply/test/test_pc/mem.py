# -*- coding:utf-8 -*-
"""
@Time: 2022/10/25
@Description:
"""

import json
import os
import subprocess
from datetime import datetime
from unittest import TestCase

import psutil

from apply.test.test_pc.model import PidInfo


# todo
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

# pstack $(pgrep "python3.7")

# 进程
# 子进程
#         线程
#             堆栈
# 评级? 嵌套?
# 对比分析 同一进程线程对比
# 不同进程对比 名与职和
# 类似 电脑排名
# 叶子节点
def exec_cmd():
    pass


def get_proc(pat: str = None):
    process_list = []
    for process in psutil.process_iter():
        process.memory_percent()
        try:
            cmdline = " ".join(process.cmdline())
        except psutil.AccessDenied as e:
            print(e)
        if pat:
            if pat in cmdline:
                process_list.append(PidInfo(
                    pid=process.pid, cmdline=cmdline, create_time=datetime.now(),
                ))
        else:
            if pat in cmdline:
                process_list.append(PidInfo(
                    pid=process.pid, cmdline=cmdline, create_time=datetime.now(),
                ))
    return process_list


class CmdResult:
    pid: str
    cmd: str
    result: str


class StackInfo:
    pid: str
    ppid: str
    thread_name: str
    method: str
    method_split: str


def get_stack(pid):
    os.system('chcp 65001')
    # children
    # memory_info 都是“rss”和“vms”
    # num_threads
    # io_counters
    # memory_maps
    pid = 4260
    cmd = f"pstack {pid}"
    # res = os.system(cmd)
    # print(res)
    with os.popen(cmd) as f:
        print(f.readlines())
    # 入库 原始的, 数据清洗后的
    return []
    # r = subprocess.Popen('wget -q -o xxx', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class TestMem(TestCase):
    def test_run(self):
        get_stack(1)
