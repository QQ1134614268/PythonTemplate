# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
import base64
import binascii
import binhex
import json
from unittest import TestCase

'''
todo 字符串, bytes, 文件, hex, 
字符串 ->  bytes
bytes -> 字符串
查看byte 使用 hex

数字转 16进制 8进制 2进制

byte 写文件: 

str 关键函数:

bytes关键函数:
    类似str, split find upper 
    encode
    hex

bytearray:

'''


class TestBase(TestCase):

    def test_number(self):
        num = 96
        print(json.dumps({
            "bin(num)": bin(num),
            "oct(num)": oct(num),
            "hex(num)": hex(num),
        }, indent=2))
        print(num & 16)

        # 原始bytes
        print(b'01', b'\x01', '01', 0x01, 0o01, '\u0101', u'01')

    def test_str(self):
        # txt = "高空瞭望"  # gb2312 没有 瞭??
        txt = "高空"
        # print(txt.encode(encoding='unicode').hex())
        print(txt.encode(encoding='utf-8').hex())
        print(txt.encode(encoding='gbk').hex())
        print(txt.encode(encoding='gb2312').hex())

    def test_bytes(self):
        num = 96
        print(bytes(num).hex())
        print(bytes([num]).hex())

        txt = "高空"
        print(bytes(txt, 'utf8').hex())

        print(b'01000000')
        print(b"\x00\x02ABC")
        print("\x00\x02ABC")

    def test_bytearray(self):
        num = 96
        print(bytearray(num))
        print(bytearray([num]))
        print(bytearray("a", "utf8"))

    def test_file(self):
        with open("a.bin", 'wb') as f:
            f.write(bytearray.fromhex("0102"))

    def test_binhex(self):
        """
            base64: bytes ->

            binascii:

            binhex:

        """
        text = "永恒a"

        b = text.encode("utf8")

        base64.b64encode(b).decode("utf8")
        base64.b64decode(b).decode("utf8")

        binascii.b2a_base64(b, newline=False).hex()
        binascii.a2b_base64("abc")

        binhex.binhex("01", "file.txt")  # 将输入文件名的二进制文件转换为binhex文件输出
        binhex.hexbin("file.txt")
