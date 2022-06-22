# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import re


def to_lower_camel(name: str):
    """下划线转小驼峰法命名"""
    return re.sub(r'_([\da-zA-Z])', lambda m: (m.group(1).upper()), name.lower())


def to_upper_camel(name: str):
    """下划线转大驼峰法命名"""
    name = to_lower_camel(name)
    return name[0:1].upper() + name[1:]


def to_snake(name: str) -> str:
    """驼峰转下划线"""
    name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    return name.lower()


if __name__ == '__main__':
    print(to_lower_camel("user0_aaIn_0f_o"))
    print(to_upper_camel("user_info"))
    print(to_snake("user0_0_aaInfo"))
    print(to_snake("user_In_fo"))
