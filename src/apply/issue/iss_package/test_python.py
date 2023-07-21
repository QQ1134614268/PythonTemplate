# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
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
