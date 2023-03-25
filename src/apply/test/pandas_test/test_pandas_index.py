from unittest import TestCase

import pandas as pd


class TestPandasIndex(TestCase):
    def test(self):
        index_a = pd.Index([1, 2, 3])
        index_b = pd.Index([2, 3, 4])
        index_a.append(index_b)
        index_a.union(index_b)  # 并集
        index_a.difference(index_b)  # 差集
        index_a.intersection(index_b)  # 交集
