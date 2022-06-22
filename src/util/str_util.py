# -*- coding:utf-8 -*-
"""
@Time: 2021/10/28
@Description:
"""
import re


def to_lower_camel(name: str):
    """下划线转小驼峰法命名"""
    return re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), name.lower())


def to_snake(name: str) -> str:
    """驼峰转下划线"""
    if '_' not in name:
        name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    else:
        raise ValueError(f'{name}字符中包含下划线，无法转换')
    return name.lower()


if __name__ == '__main__':
    print(to_snake("userInfo"))
    print(to_lower_camel("user_info"))
