# -*- coding:utf-8 -*-
"""
@Time: 2020/9/16
@Description: 
"""
import os

with open('yexingzhe.ts', 'wb') as out:
    for i in range(0, 772):
        path = os.path.join('data', "{}.ts".format(i))
        with open(path, 'rb') as f:
            out.write(f.read())
