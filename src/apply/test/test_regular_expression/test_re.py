# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import re
import unittest


class TestRe(unittest.TestCase):
    # compile 编译后 使用search, match 等,性能高;
    # findall 匹配全部; search 匹配一个,类似模板; match 从头开始匹配; full match 从头到尾匹配;

    # findall中的小括号是来定义具体匹配结果边界，也就是findall返回的是小括号中的匹配对象，而不是整个单引号中的，
    def test_findall(self):
        info = "大家好,我叫张三,英文名称:tom cat,今年12岁,手机号是:18812341234"
        ret = re.findall(r"[a-z\sA-Z]+", info)
        print(ret)

        ret = re.findall(r"\d+", info)
        print(ret)

        ret = re.findall(r"\w+", info)
        print(ret)

        ret = re.findall(r"(\d+)(\d+)", info)
        print(ret)

        ret = re.findall(r"[a-zA-Z]*", info)
        print(ret)

        # ? 非贪婪模式
        ret = re.findall(r"[a-zA-Z]+?", info)
        print(ret)

    def test_search(self):
        # search 从字符串中匹配; 可以一次匹配多个; ()代表分组,类似模板; group 是()中的取值; 匹配第一个,
        # search后 group groups 取值
        # m.group() == m.group(0)== 所有匹配的字符

        info = "大家好,我叫张三,英文名称:tom cat,我来自CHINA,今年12岁,手机号是:18812341234"
        res = re.search(r"(.*?)([a-z]+\s[a-z]+)(.*?)([A-Z]+)(.*?)(\d+)(.*?)(\d+)", info)
        print(res.group())
        print(res.group(0))
        print(res.groups())

        print(res.group(2), res.group(4), res.group(6), res.group(8))

        print(res.span())

    def test_search2(self):

        text = '我电话号，分别是13343454523， 13341154523，13341152223'

        print(re.search(r'(\d{11})', text).groups())

        print(re.search(r'(\d+)', text).groups())

        print(re.search(r'\d{11}', text).groups())

        print(re.search(r"(.+?)", text).groups())

        print(re.search(r"(.*?)", text).groups())

        print(re.search(r"(.+?)(\d+)", text).groups())

        print(re.search(r"(.+?)(\d*)", text).groups())

        print(re.search(r"(\d?)", text).groups())
