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
        # search 从字符串中匹配, 找出一个,()代表分组,可以一次匹配多个分组;类似模板; group 是()中的取值;
        # search后 group groups 取值
        # m.group() == m.group(0)== 所有匹配的字符

        info = "大家好,我叫张三,英文名称:tom cat,我来自CHINA,今年12岁,手机号是:18812341234"
        res = re.search(r"(.*?)([a-z]+\s[a-z]+)(.*?)([A-Z]+)(.*?)(\d+)(.*?)(\d+)", info)

        print("groups", res.groups())
        print("group", res.group())
        print("group_0", res.group(0))

        print(res.group(2), res.group(4), res.group(6), res.group(8))

        print("span", res.span())
        print("groupdict", res.groupdict())

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

    def test_1(self):
        info = "大家好,我叫张三,英文名称:tom cat,我来自CHINA,今年12岁,手机号是:18812341234"
        res = re.search(r"(?P<phone>\d{11})", info)
        print(res.groups(), res.group("phone"), res.groupdict())

    def test_2(self):
        #     (?!.*dataType)
        #     ?= ?<= ?! ?<!

        ret = re.findall(r"abc|def", "abcdef")
        print(ret)
        village___ = "(?P<province>[^省]+自治区|.*?省|.*?行政区|.*?市|.*?京|.*?海|.*?津)(?P<city>[^市]+自治州|.*?地区|.*?行政单位|.+盟|市辖区|.*?市|.*?县)(?P<country>[^(区|市|县|旗|岛)]+区|.*?市|.*?县|.*?旗|.*?岛)?(?P<town>[^区]+区|.+市|.+镇)?(?P<village>.*)"
        ret = re.findall(
            village___,
            "北京西城区小县")
        print(ret)

    def test_2(self):
        print(re.findall(r'<\w*?:|</\w*?:', "<wsa:a>aa<wsa:a>aa</wsa:a></wsa:a>"))
