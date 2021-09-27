# -*- coding:utf-8 -*-
"""
@Time: 2021/8/17
@Description:
"""
from elasticsearch_dsl.connections import connections
es = connections.create_connection(hosts=['127.0.0.1'])
