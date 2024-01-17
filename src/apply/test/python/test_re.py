# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import re
import unittest
'''
?P 是一个命名组的语法,用于给匹配的子模式定义一个名称 eg: (?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})
Python的re模块并不支持预查操作符,可以使用前瞻（lookahead）和后顾（lookbehind）
java不支持, 但是前瞻（lookahead）：(?=...);后顾（lookbehind）：(?<=...)
  
# 使用前瞻  
pattern = r'(?=abc)'  
string = 'abcdef'  
match = re.search(pattern, string)  
if match:  
    print('前瞻匹配成功')  
  
# 使用后顾  
pattern = r'(?<=abc)'  
string = 'abcabcdef'  
match = re.search(pattern, string)  
if match:  
    print('后顾匹配成功')
'''


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

    def test_3(self):
        print(re.findall(r'<\w*?:|</\w*?:', "<wsa:a>aa<wsa:a>aa</wsa:a></wsa:a>"))

    def test_05(self):
        """
            (?P<name>pattern)语法定义了三个命名组：year、month和day。
            然后，我们使用re.search()函数来查找匹配的子模式，
            并通过match.group("name")语法来获取每个命名组的值。
        """
        pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
        text = "The date is 2023-07-19."

        match = re.search(pattern, text)
        if match:
            year = match.group("year")
            month = match.group("month")
            day = match.group("day")
            print(f"{year} {month} {day}")  # 输出：2023 07 19

    def test06(self):

        def precheck_demo(text, pattern):
            # 首先检查是否匹配预查模式
            if re.search(pattern, text):
                # 如果预查匹配成功，再进行主模式的匹配
                match = re.search(r'\bapple\b', text)
                if match:
                    return match.start()
            return None

        text = "I have a not so good apple. I like not the reddest apple. The apple is not round."
        pattern = r'(?<!not )apple'
        demo = precheck_demo(text, pattern)
        print(demo)  # 输出: 10

    def test07(self):
        def positive_lookbehind_demo(text, pattern):
            # 首先检查是否匹配正向肯定否定预查模式
            if re.search(pattern, text):
                # 如果预查匹配成功，再进行主模式的匹配
                match = re.search(r'\bapple\b', text)
                if match:
                    return match.start()
            return None

        text = "I have a not so good apple. I like not the reddest apple. The apple is not round."
        pattern = r'(?<!not )apple'
        print(positive_lookbehind_demo(text, pattern))  # 输出: 10

    def test08(self):
        def negative_lookahead_demo(text, pattern):
            # 首先检查是否匹配负向肯定否定预查模式
            if re.search(pattern, text):
                # 如果预查匹配成功，再进行主模式的匹配
                match = re.search(r'\bapple\b', text)
                if match:
                    return match.start()
            return None

        text = "I have a not so good apple. I like not the reddest apple. The apple is not round."
        pattern = r'(?!not )apple'
        print(negative_lookahead_demo(text, pattern))

    def test09(self):
        pattern = r'(\b[\u4e00-\u9fa5]{2,5}(省|市|自治区|特别行政区)\b|\b[\u4e00-\u9fa5]{2,7}(区|县|州|市辖区)\b|\b[\u4e00-\u9fa5]{2,7}(镇|乡)\b|\b[\u4e00-\u9fa5]{2,7}(村|街道|社区)\b)'
        address = "我是广东省广州市天河区石牌镇石牌村的人"

        matcher = re.finditer(pattern, address)

        for match in matcher:
            print(match.group())

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

    def test11(self):
        # 预查操作符主要用于查找或预测某些信息，它可以根据指定的模式在文本中查找匹配项，但不会消耗字符，也就是说不会移动正则表达式的位置。
        # 前瞻操作符则是一种特殊类型的正则表达式运算符，用于指定需要满足的条件。它允许您指定一个模式，并检查该模式是否存在于后续的文本中。如果满足条件，则匹配成功，否则匹配失败。
        # 使用预查操作符查找以"a"开头并以"b"结尾的字符串
        pattern1 = r'(?=a.*b)'
        text = 'abc'
        match1 = re.search(pattern1, text)
        if match1:
            print('Match found:', match1.group())
        else:
            print('No match found')

            # 使用前瞻操作符查找以数字开头，后面跟着至少一个小写字母，再后面是至少一个大写字母的字符串
        pattern2 = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$'
        text = '123AbC'
        match2 = re.match(pattern2, text)
        if match2:
            print('Match found:', match2.group())
        else:
            print('No match found')
