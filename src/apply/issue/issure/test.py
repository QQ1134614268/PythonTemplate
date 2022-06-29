# -*- coding:utf-8 -*-
"""
@Time: 2022/6/28
@Description:
"""
from unittest import TestCase


class NewObj:
    name = ""
    uid = ""
    sim_uid = ""
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


class Flow(NewObj):
    args = []
    methods = []
    next_steps = []


class Method(NewObj):
    sim_uid = "策略"
    pass


class 翻译策略:
    is_leaf = False
    pass


class 百度翻译:
    is_leaf = True
    group_name = "翻译策略"
    pass


class 谷歌翻译:
    is_leaf = True
    group_name = "翻译策略"
    pass


class Format:
    is_leaf = True
    group_name = "翻译策略"
    pass


class CodeFlow(Flow):
    sim_uid = "code_start"
    args = ["姓名,年龄,性别, 现居住地"]
    methods = 翻译策略(百度翻译, 谷歌翻译)

    result = []

    next_steps = []  # 不停加入策略 , 形成map-reduce, 生成策略文档 (重要,方便修改 重组)


class TestAutoCode(TestCase):

    def test_run(self):
        pass
