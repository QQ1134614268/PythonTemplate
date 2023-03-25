from unittest import TestCase

import numpy as np
import pandas as pd
from pandas import DataFrame


class TestPandas(TestCase):
    def test_df_create(self):
        print({
            "df1": DataFrame({"a": [1, 2, 3], "b": [1, 2, 3], "c": [1, 2, 3]}),
            "df2": DataFrame({"one": pd.Series([1, 2], index=["a", "b"]), "two": pd.Series([4, 5], index=["b", "c"])}),
            "df3": DataFrame.from_dict({"a": [1, 2], "b": [1, 2], "c": [1, 2]}, orient="index"),  # orient: index colum,
            "df4": DataFrame([{"a": 1, "b": 2}, {"c": 3, "d": 4}])  # 横向的,
        })

    def test_df_prop(self):
        d = {"a": [1, 2, 3], "b": [1, 2, 3], "c": [1, 2, 3]}
        df = DataFrame(d)  # DataFrame(d, columns=["a1", "b1", "c1"], index=range(1, 3))
        print({
            "df": df,
            "index": df.index,
            "columns": df.columns,
            "values": df.values,
            "df.columns.tolist()": df.columns.tolist(),
        })

    def test_df_select(self):
        df = pd.DataFrame(np.arange(0, 20).reshape((4, 5)), columns=list("ABCDE"), index=range(1, 5))
        # data.loc[行索引]
        # data.loc[:, 列名]
        # data.loc[行索引, 列名]
        # data.loc[data[“某个列名”] > 6]
        print({
            "df": df,
            "df[['A', 'B']]": df[['A', 'B']],

            "df.loc[1]": df.loc[1],  # 选取
            "df.loc[:, 'A']": df.loc[:, 'A'],  # 等价于data.iloc[:, 0]
            "df.loc[:, ['A', 'B']]": df.loc[:, ['A', 'B']],  # 等价于data.iloc[:, [0, 1]]
            "df.loc[1,'A']": df.loc[1, 'A'],
            "df.loc[1:3, ['A','B','C']]": df.loc[1:3, ['A', 'B', 'C']],
            "df['A'][1]": df['A'][1],
            "df.iloc[0]": df.iloc[0],
            "df.iloc[0:2]": df.iloc[0:2],

            "切片 df.columns[1:3]": df.columns[1:3],
            "切片 df.index[1:3]": df.index[1:3],

            "df.at[1, 'A']": df.at[1, 'A'],
            "df.iloc[0].at['A']": df.iloc[0].at['A'],
            "df.iat[0, 0]": df.iat[0, 0],
        })

    def test_df_select2(self):
        df = pd.DataFrame(np.arange(0, 20).reshape((4, 5)), columns=list("ABCDE"), index=range(1, 5))
        print(df["A"] > 10)
        print((df["A"] > 10) & df["B"].apply(lambda x: x > 5))
        print(df[(df["A"] > 10) & df["B"].apply(lambda x: x > 5)])

        print(type(df.iat[0, 0]))

        print(df.where(df.notnull(), None))
        print(df.where(df.notna(), None))
        print(df.notnull())
        print(df.notna())

    def test_df_operation(self):  # 加减 赋值
        df = pd.DataFrame(np.arange(0, 6).reshape((2, 3)), columns=list("ABC"), index=range(1, 3))
        # df.copy()
        df["F"] = "f"
        df["G"] = df["A"][:1]  # NaN 补全
        print(df)
        df.insert(0, "H", pd.Series([1, 2]))  # 插入  insert(self, loc, column, value)
        print(df)

        print("----------")  # 选取
        print(df.drop(labels=["A"], axis=1, index=None, columns=None, inplace=False))  # 去除A列后的 df; inplace 原地修改
        print(df.pop('C'))  # 原地改变

        print(df.index.delete([1]))
        print("=====")
        print(df)

    def test_df_mapReduce(self):
        # 移动窗口 分组, 组内函数 count
        df = pd.DataFrame(np.random.randint(0, 5, (10, 4)), columns=list("abcd"), index=range(10))
        print("apply----", df["a"].apply(lambda x: x + 5))
        print("窗口函数", df.cumsum().rolling(window=3).mean())
        # print("窗口函数", s1.rolling(window=3).apply(lambda x: x + 1)) # todo bug

        print("group-head-----", df.groupby('b').describe())
        print(
            {
                "groupby": df.groupby('b'),
                "describe": df.groupby('b').describe(),
                "head": df.groupby('b').head(),
                "count": df.groupby('b').count(),
                "reset_index": df.groupby('b').count().reset_index(),
                "mean": df.groupby(['a', 'b']).mean(),
                # "agg": df.groupby(df['b']).agg(lambda x: x + 1), # todo bug
                # "agg_mean": df.groupby(df['b']).agg([lambda x: x + 1, 'mean']),
                "transform": df.groupby('b').transform('mean'),
            }, sep='\n'
        )
        print("# DataFrame 协方差", df.cov())
