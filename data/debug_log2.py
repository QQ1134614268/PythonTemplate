# -*- coding:utf-8 -*-
"""
@Time: 2021/7/21
@Description:
"""
import json

if __name__ == '__main__':
    ret = []
    with open("log/warn.log", 'r', encoding="utf-8")as f:
        text_lines = f.readlines()
        for line in text_lines:
            if "基础信息存在异常" in line:
                a = json.loads(line).get("msg")
                a = a.split(":")[1].split(",")[0]
                if a not in ret:
                    ret.append(a)
    print()
