# -*- coding:utf-8 -*-
"""
@Time: 2021/7/30
@Description:
"""
import unittest

from util.my_util import MyStrUti


class TestFieldMain(unittest.TestCase):

    def run_(self, lines):
        lines = lines.split("\n")
        lines = MyStrUti._stripe(lines)
        ret = []
        template = '{{"jsonField": "{}", "dbField": "{}"}},'
        for index, line in enumerate(lines):
            ret.append(template.format(line, line))
        for i in ret:
            print(i)

    def test_1(self):
        lines = """biz_date 
stk_code 
dividend_type 
stk_name 
declare_date 
ds_plan 
equity_base 
bonus_ratio 
conv_ratio 
cash_ratio 
bonus_qty 
conv_qty 
cash_balance 
r_rec_date 
xr_date 
div_date 
bonus_r_date 
conv_r_date 
new_listing_date 
tax 
taxed_div_ratio 
distribution_target 
schedule 
dmeeting_plan_date 
dmeeting_ds_plan 
equity_base2 
gmeeting_plan_date 
gmeeting_ds_plan 
allo_equity 
cancel_div_date 
memo 
gmeeting_ds_plan
allo_equity
cancel_div_date
memo
        """
        self.run_(lines)
