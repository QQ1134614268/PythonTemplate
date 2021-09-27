# -*- coding:utf-8 -*-
"""
@Time: 2021/7/30
@Description:
"""
import unittest

from util.MyUtil import MyStrUti


class TestFieldMain(unittest.TestCase):

    def run_(self, lines):
        lines = lines.split("\n")
        lines = MyStrUti._stripe(lines)
        ret = []
        template = """vo.get{}(),"""
        for index, line in enumerate(lines):
            line = MyStrUti.first_letter_case(line)
            ret.append(template.format(line))
        for i in ret:
            print(i)

    def test_1(self):
        lines = """market
        stkCode
        stkShortName
        annoDay
        windRegist
        windExcept
        windReceiptDate
        windCashPerShare
        windBonusPerShare
        sharePlan
        bonusType
        targetMarket
        targetCode
        """
        self.run_(lines)

    def test_2(self):
        lines = """market
                stkCode
                stkShortName
                
                windRegist
                windExcept
                windReceiptDate
                windCashPerShare
                windBonusPerShare
                sharePlan
                bonusType
                targetMarket
                targetCode
        """
        self.run_(lines)

    def test_3(self):
        lines = """market
        stkCode
        stkShortName
        bonusType
        windRegist
        windCashPerShare
        windBonusPerShare

        """
        self.run_(lines)
