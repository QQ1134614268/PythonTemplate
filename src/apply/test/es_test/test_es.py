# -*- coding:utf-8 -*-
"""
@Time: 2021/8/17
@Description:
"""

import unittest

import time
from elasticsearch.client import Elasticsearch


# elasticsearch中查询类型，term、match、match_all、multi_match、range、bool、boosting等区别
# https://blog.csdn.net/LeoHan163/article/details/126433158

class Es(unittest.TestCase):

    def setUp(self) -> None:
        # import os
        # os.system(r"D:\dev\elasticsearch-7.14.0\bin\elasticsearch.bat")

        self.test_index = "test_index_db"
        self.es = Elasticsearch(hosts=['ggok.top'])

    def test_main(self):
        es = self.es
        index = self.test_index

        if not es.indices.exists(index=index):  # 会返回布尔值
            es.create(index, 3, {"name": "tom2", "age": 11})

        es.index(index=index, document={"name": "tom", "age": 10}, id=1)
        es.index(index=index, document={"name": "tom2", "age": 11}, id=2)
        res = es.get(index=index, id=1)
        es.update(index=res['_index'], id=res['_id'], doc={"name": "tom2+update3", "age": 11, "time": str(time.time())})

        # 全量搜索
        res = es.search()
        res = es.search(index=index)
        # es.search(index=index, body={})
        # es.indices.delete('test_index_db') # 删除索引

        # 删除数据
        # es.delete(index, 1)
        # es.delete_by_query(index, body={})

    def test_search(self):
        es = self.es
        # 查询所有数据
        res = es.search()

        # 等于查询 term与terms, 查询 name='tom cat' 这个值不会分词必须完全包含
        res = es.search(index=self.test_index, size=20, body={
            "term": {
                "name": "tom cat"
            }
        })

        # 等于查询 term与terms, 查询 name='tom' 或 name='lili'
        res = es.search(index=self.test_index, size=20, body={
            "terms": {
                "name": ["tom", "lili"]
            }
        })

        # 包含查询，match与multi_match
        # match: 匹配name包含"tom cat"关键字的数据, 会进行分词包含tom或者cat的
        res = es.search(index=self.test_index, size=20, body={
            "match": {
                "name": "tom cat"
            }
        })

        # multi_match: 在name或info里匹配包含little的关键字的数据
        res = es.search(index=self.test_index, size=20, body={
            "multi_match": {
                "query": "little",
                "fields": ["name", "info"]
            }
        })

        # ids , 查询id 1, 2的数据 相当于mysql的 in
        res = es.search(index=self.test_index, size=20, body={
            "ids": {
                "values": ["1", "2"]
            }
        })

        # 复合查询bool , bool有3类查询关系，must(都满足),should(其中一个满足),must_not(都不满足)
        # name包含"tom" and term包含 "18"
        res = es.search(index=self.test_index, size=20, body={
            "bool": {
                "must": [
                    {
                        "term": {
                            "name": "tom",
                        },
                    },
                    {
                        "term": {
                            "age": 18,
                        },
                    },
                ]
            }
        })

        # name包含"tom" or term包含"19"
        res = es.search(index=self.test_index, size=20, body={
            "bool": {
                "should": [
                    {
                        "term": {
                            "name": "tom",
                        },

                    },
                    {
                        "term": {
                            "age": 19,
                        },

                    },
                ]
            }
        })

        # 切片式查询
        res = es.search(index=self.test_index, size=20, from_=2, body={
            "bool": {
                "should": [
                    {
                        "term": {
                            "name": "tom",
                        },

                    },
                    {
                        "term": {
                            "age": 19,
                        },
                    },
                ]
            }
        })

        # 范围查询
        res = es.search(index=self.test_index, size=20, body={
            "range": {
                "age": {
                    "gte": 18,  # >=18
                    "lte": 30  # <=30
                }
            }
        })

        # 前缀查询
        res = es.search(index=self.test_index, size=20, body={
            "prefix": {
                "name": "tom"
            }
        })

        # 通配符查询
        res = es.search(index=self.test_index, size=20, body={
            "wildcard": {
                "name": "*i"
            }
        })

        # count, 执行查询并获取该查询的匹配数
        res = es.count(index=self.test_index)

        # 短语匹配 match_phrase (搜索is a little的短语,不进行切分)
        res = es.search(index=self.test_index, size=20, body={
            "match_phrase": {
                "name": "is a little"
            }
        })

    def tear_down(self):
        self.es.close()
