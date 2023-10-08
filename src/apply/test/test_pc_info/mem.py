# -*- coding:utf-8 -*-
"""
@Time: 2022/10/25
@Description:
"""

import os
import subprocess
from datetime import datetime
from unittest import TestCase

import psutil

from apply.test.test_pc_info.model import PidInfo


# todo 内存
def exec_cmd():
    pass


def get_proc(pat: str = None):
    process_list = []
    for process in psutil.process_iter():
        process.memory_percent()
        try:
            cmdline = " ".join(process.cmdline())
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
        except psutil.AccessDenied as e:
            print(e)
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
