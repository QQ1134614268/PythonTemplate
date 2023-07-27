# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
import binascii
import binhex
import json
from unittest import TestCase


class TestBase(TestCase):

    def test_run(self):
        num = 127
        print(json.dumps({
            "bin(num)": bin(num),
            "oct(num)": oct(num),
            "hex(num)": hex(num),
        }, indent=2))
        print("bytes(num): ", bytes(num))
        print("bytes([num]): ", bytes([num]))
        print("bytes('a', 'utf8'): ", bytes('a', 'utf8'))
        print(b'01000000')
        print(b"\x00\x02ABC")
        print("\x00\x02ABC")
        print(bytes("\x00\x02ABC", 'utf8'))

        print(bytearray(num))
        print(bytearray([num]))
        print(bytearray("a", "utf8"))

        print(num & 16)

        print(b'01', b'\x01', '01', 0x01, 0o01, '\u0101', u'01')

        with open("a.bin", 'wb') as f:
            f.write(bytearray.fromhex("0102"))

        binascii.a2b_base64("01")
        binhex.binhex("01", "file.txt")  # 将输入文件名的二进制文件转换为binhex文件输出

        # 十进制	八进制	十六进制	二进制	符号	HTML实体	说明
        # 0	000	00	00000000	NUL	&#000;	空字符
