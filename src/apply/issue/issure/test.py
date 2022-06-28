# -*- coding:utf-8 -*-
"""
@Time: 2022/6/28
@Description:
"""


class NewObj:
    name = ""
    uid = ""
    desc = ""
    sort = ""


class Str(NewObj):
    regx = ""
    length = ""
    nullable = ""
    pass


class Num(Str):
    # 区间
    area = ""


class DateTime(Num):
    pass
