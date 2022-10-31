import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser = Series([1, 2, 3])
ser = Series(np.array([1, 2, 3]))
ser = Series({"a": 1, "b": 1})
ser = Series({"a": 1, "b": 1}, index=["a", "b", "d"])  # index 筛选,不补全

print({
    "ser[a]": ser["a"],
    "ser['a', 'b', 'c']": ser[["a", "b", "c"]],
    "ser.a": ser.a,
    "ser.index": ser.index,
    "ser.values": ser.values,
})

d = {"a": [1, 2, 3], "b": [1, 2, 3], "c": [1, 2, 3]}
df = DataFrame(d)
df2 = DataFrame(d, columns=["b", "a", "d"])

print({
    "df": df,
    "df2": df2,
    "index": df.index,
    "columns": df.columns,
    "values": df.values,

})
d2 = {"one": pd.Series([1, 2, 3], index=["a", "b", "c"]), "two": pd.Series([4, 5, 6], index=["b", "c", "d"])}
df3 = DataFrame(d2)
df4 = DataFrame(d2, index=["c", "d", "e"])
df5 = DataFrame.from_dict(d2, orient="index")  # orient: index colum
df6 = DataFrame([{"a": 1, "b": 2}, {"c": 3, "d": 4}])  # 横向的
df7 = pd.DataFrame(np.random.randn(4, 5), columns=list("ABCDE"), index=range(1, 5))

print({
    "df3": df3,
    "df4": df4,
    "df5": df5,
    "df6": df6,
    "df7": df7,
    "df7.loc[1]": df7.loc[1],  # 选取
    "df7.loc[1,'A']": df7.loc[1, 'A'],
    "df7['A'][1]": df7['A'][1],
    "df7.iloc[0:2]": df7.iloc[0:2],
})

df = pd.DataFrame(np.random.random(4, 5), columns=list("ABCDE"), index=range(1, 5))

df.drop(["A"], axis=1)  # 选取 , inplace=True
df.drop(1, inplace=True)  # inplace=True 原地改变
ret = df.pop('B')  # 原地改变
df["F"] = "f"
df["G"] = df["c"][:2]  # NaN 补全
df.insert(0, "i0", pd.Series([1, 2]))  # 插入

df = pd.DataFrame(np.random.randn(8, 4), index=pd.date_range('1/1/2022', periods=8), columns=list("ABCD"))
index = df.index  # 时间类型index, 不可赋值
index[1:3]
index.delete([0, 2])
index.drop(2)
index.insert((1, "k5"))

index_a = pd.Index([1, 2, 3])
index_b = pd.Index([2, 3, 4])
index_a.append(index_b)
index_a.union(index_b)  # 并集
index_a.difference(index_b)  # 差集
index_a.intersection(index_b)  # 交集

df = pd.DataFrame(np.random.randn(8, 4), index=pd.date_range('1/1/2022', periods=8), columns=list("ABCD"))
df.loc['2022-01-01']
df.loc['2022-01-01': '2022-01-04', ['A', 'C']]
df.loc[df['A'] > 0]  # 选取 filter condition

df.iloc[0]
df.iloc[[0, 4], 1:3]
# df.iloc[df['A']>0]

# 移动窗口 分组, 组内函数 count
series_1 = Series(np.random.randn(10))
series_2 = Series(np.random.randn(10))
series_1.cov(series_2)  # 协方差

df = DataFrame(np.random.randn(4, 5), index=[1, 2, 3, 4], columns=list("ABCDE"))
df.cov()

s1 = Series(np.random.randn(10), index=pd.date_range("1/1/2022", 10))
ret = s1.cumsum().rolling(window=3)
ret.mean()[2:5]

pd.DataFrame(np.random.randn(10, 4), index=pd.date_range("1/1/2022", periods=10), columns=list("ABCD"))

df["A"].apply(lambda x: x + 1)
df.rolling(window=3, min_periods=2).apply(lambda x: x.max - x.min())

df = DataFrame({'a': list('abcad'), 'b': ["a", 'b', 'a', 'b', 'a'], 'c': np.random.randn(5), 'd': np.random.randn(5)})
df.groupby('b')
df.groupby('b').count()
df.groupby('b').count().reset_index()  # 拉平
df.groupby(['a', 'b']).mean()
df.groupby('b').describe()
df.groupby('b').head()

df.groupby(df['b']).agg(lambda x: x + 1)
df.groupby(df['b']).agg([lambda x: x + 1, 'mean'])
df.groupby('b').transform('mean')
