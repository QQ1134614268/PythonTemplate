# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import re
import unittest


class TestRe(unittest.TestCase):
    # findall 匹配全部, 返回list
    # search 匹配一个, 返回Match, 模板匹配,只返回()中内容
    # match 从头开始匹配;
    # full_match 从头到尾匹配;
    # compile 编译后 使用search, match 等,性能高;

    # ()类似模板, 返回括号中匹配内容;
    
    def test_findall(self):
        info = "大家好,我叫张三,英文名称:tom cat,今年10岁,手机号是:18812341234"

        ret = re.findall(r"\d+", info)
        print(ret)
        ret = re.findall(r"手机号是:\d+", info)
        print(ret)
        ret = re.findall(r"手机号是:(\d+)", info)  # 只返回括号中内容, 模板匹配
        print(ret)
        ret = re.findall(r"[a-z]+", info)  # []
        print(ret)

        ret = re.findall(r"[a-z]+?", info)  # ? 非贪婪模式
        print(ret)

        # | 或者: 多个表达式
        ret = re.findall(r"\d+|[a-z]+", info)  # ['tom', 'cat', '12', '18812341234']
        print(ret)

        # | () 组合
        ret = re.findall(r"(\d+)|[a-z]+", info)  # ['', '', '12', '18812341234']
        print(ret)
        ret = re.findall(r"(\d+)|([a-z]+)", info)  # [('', 'tom'), ('', 'cat'), ('12', ''), ('18812341234', '')]
        print(ret)

    def test_search(self):
        # m.group() == m.group(0)== 所有匹配的字符

        info = "大家好,我叫张三,英文名称:tom cat,我来自CHINA,今年10岁,手机号是:18812341234"

        print(re.search(r'\d+', info).groups())  # 没有(), 返回空元祖
        print(re.search(r'(\d+)', info).groups())

        res = re.search(r"我叫(.+?),.*?名称:([a-z]+\s*?[a-z]+)", info)
        print("groups:", res.groups())
        print("group:", res.group(), res.group(0), res.group(1))
        print("span:", res.span())
        print("groupdict:", res.groupdict())

    def test_high_namespace(self):
        # ?P 是一个命名组的语法,用于给匹配的子模式定义一个名称 eg: (?P<phone>\d{11})

        info = "大家好,我叫张三,英文名称:tom cat,我来自CHINA,今年10岁,手机号是:18812341234"
        res = re.search(r"(?P<phone>\d{11})", info)
        print(res.groups(), res.group("phone"), res.groupdict())

    def test_high_(self):
        """
             ?=   正向肯定 positive_lookbehind
             ?!   正向否定
             ?<=  负向肯定
             ?<!  负向否定
             
            零宽断言, preCheck        
        """
        info = "大家好,我叫张三,英文名称:tom cat,我来自CHINA,今年10岁,手机号是:18812341234"
        res = re.findall(r"(?=188)(\d+)", info)  # 正向, 以188开头数字
        print(res)
        res = re.findall(r"(?!188)(\d+)", info)  # 正向, 不以188开头数字
        print(res)

        res = re.findall(r"(?<=188)(\d+)", info)  # 负向, 以188开头数字
        print(res)
        res = re.findall(r"(?<!今年)(\d+)", info)  # 负向, 不以188开头数字
        print(res)

    def test10(self):
        # 定义正则表达式模式
        pattern = r'\b[\u4e00-\u9fa5][\u4e00-\u9fa5]*\b'
        # “\b”是一个特殊的元字符，表示单词边界。它用来设置单词的界限，匹配单词的开始或结束。
        # 待匹配的文本
        text = '我来自 中国，我喜欢学 习 编程。'

        # 使用re.findall()函数进行匹配
        matches = re.findall(pattern, text)

        # 输出匹配结果
        for match in matches:
            print('匹配的汉语单词:', match)
