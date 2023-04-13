# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import unittest
from xml.etree import ElementTree


class TestXml(unittest.TestCase):

    def test_xml(self):
        with open("C:\\Users\\Administrator\\Desktop\\out.xml.log", mode="r") as f2:
            for line in f2.readlines():
                with open("tmp.xml", mode="w") as f3:
                    f3.write(line)
                tree = ElementTree.parse("tmp.xml")
                root = tree.getroot()
                print(tree, root, root.tag, root.attrib, root.text, root.tail, root.getchildren())
