# -*- coding:utf-8 -*-
"""
@Time: 2021/7/13
@Description:
"""
import pandas as pd

data = {'省份': ['北京', '上海', '广州', '深圳'],
        '年份': ['2017', '2018', '2019', '2020'],
        '总人数': ['2200', '1900', '2170', '1890'],
        '高考人数': ['6.3', '5.9', '6.0', '5.2']}
df = pd.DataFrame(data, columns=['省份', '年份', '总人数', '高考人数', '高数'],
                  index=['one', 'two', 'three', 'four'])
df['高数'] = ['90', '95', '92', '98']
print("行索引：{}".format(list(df.index)))
print("列索引：{}".format(list(df.columns)))
print(df.index[1:3])
print(df.columns[1])
print(df.columns[1:3])
print(df)
df.columns.tolist()

# ======================================
from pandas import Series
emp = ['01', '02', '03', '04', '05', '06']
name = ['小乔', '孙策', '刘备', '赵云', '哪吒', '张飞']
# 构建数据
series = Series(data=name, index=emp)
series.values
series.index
list(series.index)
series.items
list(series.items())
list(series.keys())
