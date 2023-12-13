# -*- coding:utf-8 -*-
import time
from itertools import chain
from typing import List
from zipfile import ZipFile


def all_passwd(dictionary: List[str], max_len: int):
    # 返回由 dictionaries 中字符组成的所有长度为 max_len 的字符串

    def helper(temp: list, begin: int, n: int):
        # 辅助函数，是个生成器
        if begin == n:  # 达到递归出口
            yield ''.join(temp)
            return
        for t in dictionary:
            temp[begin] = t  # 在每个位置
            yield from helper(temp, begin + 1, n)

    yield from helper([0] * max_len, 0, max_len)


def extract(zip_file: ZipFile, pwd: str) -> bool:
    # zip_file: 一个ZipFile类, pwd: 密码
    try:
        zip_file.extractall(path='', pwd=pwd.encode('utf-8'))  # 密码输入错误的时候会报错
        print(f"Password is: {pwd}")  # 将正确的密码输出到控制台
        return True
    except Exception as e:
        print(e)
        return False
    # 用 bool 类型的返回值告诉主程序是否破解成功 (意思就是返回 True 了以后就停止)


def method_name():
    global start, total
    start = time.time()
    # chr(97) -> 'a' 这个变量保存了密码包含的字符集
    dictionaries = [chr(i) for i in chain(range(97, 123), range(65, 91), range(48, 58))]  # 0 - 9
    # dictionaries.extend(['.com', 'www.'])  # 添加自定义的字符集
    lengths = [6, 2, ]  # 密码长度
    total = sum(len(dictionaries) ** k for k in lengths)  # 密码总数
    file_name = 'test.zip'
    zip_file2 = ZipFile(file_name, 'r')  # 很像open
    for max_len in lengths:
        for pwd2 in all_passwd(dictionaries, max_len):
            if extract(zip_file2, pwd2):  # 记得extract函数返回的是bool类型的哦
                return True


if __name__ == '__main__':
    method_name()
