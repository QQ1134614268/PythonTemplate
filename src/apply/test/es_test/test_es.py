# -*- coding:utf-8 -*-
"""
@Time: 2021/8/17
@Description:
"""

import json
import unittest
import uuid
from datetime import datetime

from elasticsearch import helpers
from elasticsearch_dsl.connections import connections


class Es(unittest.TestCase):

    def setUp(self) -> None:
        import os
        os.system(r"D:\dev\elasticsearch-7.14.0\bin\elasticsearch.bat")
        self.es = connections.create_connection(hosts=['127.0.0.1'])
        self.test_index = "test_index_db"
        self.test_doc_type = "student_table"
        self.test_id = 1
        self.test_data = {'id': 1, 'name': '张三'}
        self.data = {
            '_index': self.test_index,
            '_type': self.test_doc_type,
            '_id': self.test_id,
            '_body': self.test_data
        }

    def tear_down(self):
        self.es.close()

    def test_run(self):
        es = self.es
        # 创建索引，索引的名字是my-index,如果已经存在了，就返回个400，
        # 这个索引可以现在创建，也可以在后面插入数据的时候再临时创建
        # es.indices.create(index='my-index')
        es.index(index="my-index", doc_type="test-type", id=1, body={"any": "data1", "timestamp": datetime.now()})

        # 插入数据,(这里省略插入其他两条数据，后面用)
        res = es.index(index="my-index", doc_type="test-type", id=2, body={"any": "data1", "timestamp": datetime.now()})
        # 查询数据，两种get and search
        # get获取
        res = es.get(index="my-index", doc_type="test-type", id=1)
        res = es.get(index='my-index', doc_type='test-type', id=2)

        # delete：删除指定index、type、id的文档
        res = es.delete(index='my-index', doc_type='test-type', id=2)

    def test_add(self):
        # 单个修改
        self.es.index(index=self.test_index, doc_type=self.test_doc_type, id=self.test_id, body=self.test_data)
        res = self.es.get(index=self.test_index, doc_type=self.test_doc_type, id=self.test_id)

        # 批量修改
        dic = {'id': uuid.uuid4().hex, 'name': '张三'}
        data = {'_index': self.test_index, '_type': self.test_doc_type, '_id': uuid.uuid4().hex, '_body': dic}
        course = [data]
        helpers.bulk(self.es, course)

    def test_update_single(self):
        body = {"doc": {"stanford": 1, "name": "update-张三"}}
        self.es.index(index=self.test_index, doc_type=self.test_doc_type, id=self.test_id, body=self.test_data)
        self.es.update(index=self.test_index, doc_type=self.test_doc_type, id=self.test_id, body=json.dumps(body))
        res = self.es.get(index=self.test_index, doc_type=self.test_doc_type, id=self.test_id, )

    def test_sea(self):
        # 查询所有数据
        # 方法1
        # res = es.search(index='test6', size=20)
        # 方法2
        res = self.es.search(index='person', size=20, body={
            "query": {
                "match_all": {}
            }
        })
        print(json.dumps(res, indent=4))
        es = self.es
        # 等于查询 term与terms, 查询 name='tom cat' 这个值不会分词必须完全包含
        res = es.search(index='test6', size=20, body={
            "query": {
                "term": {
                    "name": "tom cat"
                }
            }
        })

        # 等于查询 term与terms, 查询 name='tom' 或 name='lili'
        res = es.search(index='test6', size=20, body={
            "query": {
                "terms": {
                    "name": ["tom", "lili"]
                }
            }
        })

        # 包含查询，match与multi_match
        # match: 匹配name包含"tom cat"关键字的数据, 会进行分词包含tom或者cat的
        res = es.search(index='test6', size=20, body={
            "query": {
                "match": {
                    "name": "tom cat"
                }
            }
        })

        # multi_match: 在name或info里匹配包含little的关键字的数据
        res = es.search(index='test6', size=20, body={
            "query": {
                "multi_match": {
                    "query": "little",
                    "fields": ["name", "info"]
                }
            }
        })

        # ids , 查询id 1, 2的数据 相当于mysql的 in
        res = es.search(index='test6', size=20, body={
            "query": {
                "ids": {
                    "values": ["1", "2"]
                }
            }
        })

        # 复合查询bool , bool有3类查询关系，must(都满足),should(其中一个满足),must_not(都不满足)
        # name包含"tom" and term包含 "18"
        res = es.search(index='test6', size=20, body={
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
            }
        })

        # name包含"tom" or term包含"19"
        res = es.search(index='test6', size=20, body={
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
            }
        })

        # 切片式查询
        res = es.search(index='test6', size=20, body={
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
            "from": 2,  # 从第二条数据开始
            "size": 4,  # 获取4条数据
        })

        # 范围查询
        res = es.search(index='test6', size=20, body={
            "query": {
                "range": {
                    "age": {
                        "gte": 18,  # >=18
                        "lte": 30  # <=30
                    }
                }
            }
        })

        # 前缀查询
        res = es.search(index='test6', size=20, body={
            "query": {
                "prefix": {
                    "name": "tom"
                }
            }
        })

        # 通配符查询
        res = es.search(index='test6', size=20, body={
            "query": {
                "wildcard": {
                    "name": "*i"
                }
            }
        })

        # 排序
        res = es.search(index='test6', size=20, body={
            "query": {
                "wildcard": {
                    "name": "*i"
                }
            },
            "sort": {
                "age": {
                    "order": "desc"  # 降序
                }
            }
        })

        # count, 执行查询并获取该查询的匹配数
        c = es.count(index='test6')
        print(c)

        # 短语匹配 match_phrase (搜索is a little的短语,不进行切分)
        res = es.search(index='test6', size=20, body={
            "query": {
                "match_phrase": {
                    "name": "is a little"
                }
            }
        })
