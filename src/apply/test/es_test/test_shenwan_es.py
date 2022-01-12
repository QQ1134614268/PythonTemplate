# -*- coding:utf-8 -*-
"""
@Time: 2021/8/17
@Description:
"""

import unittest

from elasticsearch.client import Elasticsearch


class Es(unittest.TestCase):

    def setUp(self) -> None:
        self.test_index = "es_stock_list"
        self.es = Elasticsearch(hosts=['124.71.68.9:30093'])

    def test_main(self):
        es = self.es
        index = self.test_index
        # res = es.get(index=index)
        res = es.search(index=index)
        print()
