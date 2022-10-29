# -*- coding:utf-8 -*-
"""
@Time: 2021/7/13
@Description:
"""
from pandas import Series

import numpy as np
import pandas as pd

from unittest import TestCase


class TestAutoCode(TestCase):
    def test_Series(self):
        emp = ['01', '02', '03', '04', '05', '06']
        name = ['小乔', '孙策', '刘备', '赵云', '哪吒', '张飞']
        # 构建数据
        series = Series(data=name, index=emp)
        print({
            "series": series,
            "series.values": series.values,
            "series.index": series.index,
            "series.items": series.items,
            "series.keys": series.keys,
        })

    def test_run(self):
        data = {'省份': ['北京', '上海', '广州', '深圳'],
                '时间': ['2017/5/22', '2018/5/22', '2019/5/22', '2020/5/22'],
                '总人数': [2200, 1900, 2170, 1890],
                '高考人数': ['6.3', '5.9', '6.0', '5.2']
                }
        df = pd.DataFrame(data, columns=['省份', '年份', '总人数', '高考人数', '高数'],
                          index=['one', 'two', 'three', 'four'])
        # loc at iloc iat na(null)

        #

        df = df[
            (df["省份"] == "北京")
            & df["总人数"].apply(lambda x: x > 2000)
            ]

        df['高数'] = ['90', '95', '92', '98']
        print({
            "行索引 index：": list(df.index),
            "列索引 columns：": list(df.columns),
            "切片 df.index[1:3] ": df.index[1:3],
            "切片 df.columns[1:3] ": df.columns[1:3],
            "df.columns.tolist()": df.columns.tolist(),
        })

    def test_Na(self):
        # 初始化 文件, Series, dicts
        df = pd.DataFrame({
            'col_1': [0, 1, 2, 3],
            'col_2': [None, np.nan, pd.NaT, 1.5],
            'col_3': [pd.NaT, pd.NaT, pd.NaT, pd.to_datetime('2018/5/22', format='%Y/%m/%d')]
        },
            index=['row_1', 'row_2', 'row_3', 'row_4']
        )

        print(df)

        # data.loc[行索引]
        # data.loc[:, 列名]
        # data.loc[行索引, 列名]
        # data.loc[data[“某个列名”] > 6]

        print(df.at["one", 'A'])
        print(df.iloc[0].at['A'])
        print(df.iat[0, 0])

        print(type(df.iat[0, 0]), df.iat[0, 0])
        print(type(df.iat[0, 2]), df.iat[0, 2])
        print(type(df.iat[1, 2]), df.iat[1, 2])

        print(df[['A', 'B']])
        # df[0] # bug
        print(df.loc[:, 'A'])  # 等价于data.iloc[:, 0]
        print(df.loc[:, ['A', 'B']])  # 等价于data.iloc[:, [0, 1]]
        print(df.iloc[1])
        print(df.where(df.notnull(), None))
        print(df.where(df.notna(), None))
        print(df.notnull())
        print(df.notna())
