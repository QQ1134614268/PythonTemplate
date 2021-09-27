# -*- coding:utf-8 -*-
"""
@Time: 2021/7/13
@Description:
参考:  https://blog.csdn.net/ctrigger/article/details/92666982
"""
import numpy as np
import pandas as pd

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
