# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import re

# todo 正则
# 重要语法
# 函数 match search group findall


# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h", "hello Python")
res = ret.group()
print(res)

ret = re.findall("【.+?】", "【zhong】【guo】【(.+?)】")
print(ret)

# (...) 匹配括号内的任何正则表达式，并指示组的开始和结束；
ret = re.findall("【(.+?)】", "【zhong】【guo】【(.+?)】")
print(ret)

ret = re.findall("\((.+?)\)", "红灯(停),绿灯(行)")
print(ret)

ret = re.findall(r"\((.+?)\)", "红灯(停),绿灯(行)")
print(ret, "=")

ret = re.findall(r"\[(.+?)\]", "中国A股日行情估值指标[AShareEODDerivativeIndicator]")
print(ret)

pattern = re.compile("\[(.+?)\]")
text = "中国A股日行情估值指标[AShareEODDerivativeIndicator]"

pattern.search(text)
print(pattern.search(text).group())

ret = re.search("【(.+?)】", "【zhong】【guo】【(.+?)】")
print(ret)

pattern = re.compile("【(.+?)】")
txt = "【zhong】【guo】【(.+?)】"

pattern.search(text).group()

# findall中的小括号是来定义具体匹配结果边界，也就是findall返回的是小括号中的匹配对象，而不是整个单引号中的，
# search中是将小括号作为一个优先级的判断符号
