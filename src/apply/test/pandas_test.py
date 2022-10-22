# -*- coding:utf-8 -*-
"""
@Time: 2021/7/13
@Description:
"""
from pandas import Series

import numpy as np
import pandas as pd

data = {'省份': ['北京', '上海', '广州', '深圳'],
        '年份': ['2017', '2018', '2019', '2020'],
        '总人数': ['2200', '1900', '2170', '1890'],
        '高考人数': ['6.3', '5.9', '6.0', '5.2']
        }
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

# 初始化 文件, Series, dicts
df = pd.DataFrame({
    'A': [0, 1, 2, 3],
    'B': [np.nan, 2.3, 3.6, 1.5],
    'C': [pd.NaT, pd.NaT, pd.NaT, pd.to_datetime('2018/5/22', format='%Y/%m/%d')]
})

print(df)
print(df.at[0, 'A'])
print(df.iloc[0].at['A'])
print(df.iat[0, 0])

print(type(df.iat[2, 2]), df.iat[2, 2])
print(type(df.iat[0, 2]), df.iat[0, 2])
print(type(df.iat[1, 2]), df.iat[1, 2])

# a[0]、或者是a.iloc[0],iloc的意思是integer-location based indexing for selection by position
# 还有一种是key索引（我自己这么叫的），例如a.loc['title'] ，loc的意思是 label-location based indexer for selection by label。
# 这两种不同的索引暴露了Series的本质，就是pandas对象本质上是字典和列表的混合，这点很重要
print(df['A'])
print(df[['A', 'B']])
# df[0] # bug

print(df.loc[:, 'A'])  # 等价于data.iloc[:, 0]
print(df.loc[:, ['A', 'B']])  # 等价于data.iloc[:, [0, 1]]

print(df.iloc[1])

print(df.where(df.notnull(), None))
print(df.where(df.notna(), None))
print(df)
print(df.notnull())
print(df.notna())
