# -*- coding:utf-8 -*-
"""
@Time: 2021/8/17
@Description:
"""
import unittest

from elasticsearch.client import Elasticsearch


# elasticsearch中查询类型，term、match、match_all、multi_match、range、bool、boosting等区别
# https://blog.csdn.net/LeoHan163/article/details/126433158

class TestEs(unittest.TestCase):

    def setUp(self) -> None:
        # import os
        # os.system(r"D:\dev\elasticsearch-7.14.0\bin\elasticsearch.bat")

        self.test_index = "test_index_db"
        self.es = Elasticsearch(hosts=['http://127.0.0.1:9200'])  # 防火墙,网关 302

    def test_create(self):
        self.es.create(self.test_index, 1, {"name": "tom2", "age": 11})
        # es.indices.exists(index=index)

        # index 覆盖更新
        self.es.index(index=self.test_index, body={"name": "tom", "age": 10}, id=1)
        self.es.index(index=self.test_index, body={"name": "cat", "age": 11}, id=2)

        res = self.es.search(index=self.test_index)
        print(res and res["hits"] and res["hits"]["hits"])

        res = self.es.get(index=self.test_index, id=1)
        print(res)

        # self.es.update(self.test_index, 1, '_doc', params={"name": "tom2", "age": 11, "time": str(time.time())})

        # self.es.indices.delete(self.test_index) # 删除索引

        # 删除数据
        # self.es.delete(self.test_index, 1)
        # self.es.delete_by_query(self.test_index, body={})

    def test_search(self):
        # 查询所有数据
        res = self.es.search()
        print(res and res["hits"] and res["hits"]["hits"])

    def test_term(self):
        # 等于查询 term与terms, 查询 name='tom cat' 这个值不会分词必须完全包含
        res = self.es.search(index=self.test_index, body={
            "query": {
                "term": {
                    "name": "tom cat"
                }
            },
            "size": 10
        })
        print(res)

    def test_terms(self):
        # 等于查询 term与terms, 查询 name='tom' 或 name='lili'  "query": {"size":10,}
        res = self.es.search(index=self.test_index, body={
            "size": 10,
            "query": {
                "terms": {
                    "name": ["tom", "lili"]
                }
            }
        })
        print(res)

    def test_match(self):
        # 包含查询，match与multi_match
        # match: 匹配name包含"tom cat"关键字的数据, 会进行分词包含tom或者cat的
        res = self.es.search(index=self.test_index, body={
            "query": {
                "match": {
                    "name": "tom cat"
                }
            },
            "size": 10,
        })
        print(res)

    def test_multi_match(self):
        # multi_match: 在name或info里匹配包含little的关键字的数据
        res = self.es.search(index=self.test_index, body={
            "query": {
                "multi_match": {
                    "fields": ["name", "info"],
                    "query": "little",
                }
            },
            "size": 10,
        })
        print(res)

    def test_values(self):
        # values , 查询name tom, cat的数据 相当于mysql的 in
        res = self.es.search(index=self.test_index, body={
            "query": {
                "name": {
                    "values": ["tom", "cat"]
                }
            },
            "size": 10,
        })
        print(res)

    def test_bool_must(self):
        # 复合查询bool , bool有3类查询关系，must(都满足),should(其中一个满足),must_not(都不满足)
        # name包含"tom" and term包含 "18"
        res = self.es.search(index=self.test_index, body={
            "query": {
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
            },
            "size": 10,
        })
        print(res)

    def test_bool_should(self):
        # name包含"tom" or term包含"19"
        res = self.es.search(index=self.test_index, body={
            "query": {
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
            },
            "size": 10,
        })
        print(res)

    def test_range(self):
        # 范围查询
        res = self.es.search(index=self.test_index, body={
            "query": {
                "range": {
                    "age": {
                        "gte": 18,  # >=18
                        "lte": 30  # <=30
                    }
                }
            },
            "size": 10,
        })
        print(res)

    def test_prefix(self):
        # 前缀查询
        res = self.es.search(index=self.test_index, body={
            "query": {
                "prefix": {
                    "name": "tom"
                }
            },
            "size": 10,
        })
        print(res)

    def test_wildcard(self):
        # 通配符查询
        res = self.es.search(index=self.test_index, body={
            "query": {
                "wildcard": {
                    "name": "*i"
                }
            },
            "size": 10,
        })
        print(res)

    def test_count(self):
        # count, 执行查询并获取该查询的匹配数
        res = self.es.count(index=self.test_index)
        print(res)

    def test_match_phrase(self):
        # 短语匹配 match_phrase (搜索is a little的短语,不进行切分)
        res = self.es.search(index=self.test_index, body={
            "query": {
                "match_phrase": {
                    "name": "is a little"
                }
            },
            "size": 10,
        })
        print(res)

# Relational DB          Elasticsearch
# 数据库(database)         索引(indices)
# 表(tables)                 types
# 行(rows)                   documents
# 字段(columns)              fields
#
#
# method           url地址                                    描述
# PUT     localhost:9200/索引名称/类型名称/文档id        创建文档（指定文档id）
# POST    localhost:9200/索引名称/类型名称 创建文档      （随机文档id）
# POST    localhost:9200/索引名称/类型名称/文档id/_update   修改文档
# DELETE  localhost:9200/索引名称/类型名称/文档id           删除文档
# GET     localhost:9200/索引名称/类型名称/文档id           查询文档通过文档id
# POST    localhost:9200/索引名称/类型名称/_search         查询所有数
