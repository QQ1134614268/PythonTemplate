# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/2 23:04
"""
# https://www.cnblogs.com/zhehan54/p/6130030.html
import os

print('当前进程:%s 启动中 ....' % os.getpid())
# linux系统有fork()
pid = os.fork()
if pid == 0:
    print('子进程:%s,父进程是:%s' % (os.getpid(), os.getppid()))
else:
    print('进程:%s 创建了子进程:%s' % (os.getpid(), pid))
