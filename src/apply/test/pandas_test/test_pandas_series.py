# -*- coding:utf-8 -*-
"""
@Time: 2021/7/13
@Description:
"""
from unittest import TestCase

import numpy as np
from pandas import Series


class TestPandasSeries(TestCase):

    def test_series_create(self):
        print({
            "Series([1, 2, 3])": Series([1, 2, 3]),
            "Series(np.array([1, 2, 3]))": Series(np.array([1, 2, 3])),
            'Series({"a": 1, "b": 1})': Series({"a": 1, "b": 1}),
            'Series({"a": 1, "b": 1}': Series({"a": 1, "b": 1}, index=["a", "b", "d"])  # index 筛选,不补全
        })

    def test_series_prop(self):
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

    def test_series_select(self):
        ser = Series({"a": 1, "b": 1}, index=["a", "b", "d"])
        print({
            "ser": ser,
            "ser[a]": ser["a"],
            "ser.a": ser.a,
            "ser['a', 'd']": ser[["a", "d"]],
        })

    def test_series_cov(self):
        series_1 = Series(np.random.randn(3))
        series_2 = Series(np.random.randn(3))
        print("# Series 协方差", series_1.cov(series_2))
