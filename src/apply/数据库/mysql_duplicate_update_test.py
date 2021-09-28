# -*- coding:utf-8 -*-
"""
@Time: 2021/7/30
@Description:
"""
import re
import unittest

# engine 参数语法 :id
# session 参数语法 %(id)s
# connection
# cursors
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql import Insert

Base = declarative_base()


class TestTable(Base):
    # 表名称
    __tablename__ = 'test_t'
    # 表结构
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name2 = Column(String(64))


class TestMysql(unittest.TestCase):

    def setUp(self):
        # 创建对象的基类:
        # 初始化数据库连接:
        dev = "mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8"
        self.engine = create_engine(dev, echo=True)
        self.session = sessionmaker(bind=self.engine)()
        self.session.execute("select 1")  # 跳过session初始化的一些条件查询,便于后续debug

    def test_session(self):
        sql2 = '''
                INSERT INTO test_t(id,name2)
                VALUES (:id,:name2) 
                ON DUPLICATE KEY UPDATE name2 = VALUES(name2)
                '''
        data = [{'id': 1, "name2": 363},
                {'id': 2, "name2": 3}]
        # self.engine.execute(sql2, data)  # 报错 :id
        self.session.execute(sql2, data)
        self.session.commit()

    def test_engine(self):
        sql2 = '''INSERT INTO test_t(id,name2)
                   VALUES (%(id)s,%(name2)s) 
                   ON DUPLICATE KEY UPDATE name2 = VALUES(name2)
                '''
        data = [{'id': 1, "name2": 363}, {'id': 2, "name2": 3}]
        self.engine.execute(sql2, data)
        # self.session.execute(sql2, data) # 报错,  parameters: ({}, {})

    def test_many(self):
        sql1 = '''INSERT INTO test_t(id,name2)VALUES (:id,:name2) ON DUPLICATE KEY UPDATE name2 = VALUES(name2)'''
        sql2 = '''INSERT INTO test_t(id,name2)VALUES (%(id)s,%(name2)s) ON DUPLICATE KEY UPDATE name2 = VALUES(name2)'''

        RE_INSERT_VALUES = re.compile(
            r"\s*((?:INSERT|REPLACE)\b.+\bVALUES?\s*)" +
            r"(\(\s*(?:%s|%\(.+\)s)\s*(?:,\s*(?:%s|%\(.+\)s)\s*)*\))" +
            r"(\s*(?:ON DUPLICATE.*)?);?\s*\Z",
            re.IGNORECASE | re.DOTALL)
        # sql执行  批量 或者循环
        # venv/Lib/site-packages/pymysql/cursors.py:193
        m = RE_INSERT_VALUES.match(sql1)  # 匹配简单表达式
        print(bool(m))
        m = RE_INSERT_VALUES.match(sql2)  # 不匹配,mysql循环执行插入
        print(bool(m))

    def test_model0(self):
        # 参考: https://stackoverflow.com/questions/6611563/sqlalchemy-on-duplicate-key-update
        @compiles(Insert)
        def append_string(insert, compiler, **kw):
            s = compiler.visit_insert(insert, **kw)
            if 'append_string' in insert.kwargs:
                return s + " " + insert.kwargs['append_string']
            return s

        data = [{'id': 1, "name2": 363}, {'id': 2, "name2": 3}]
        sql = insert(TestTable, append_string='ON DUPLICATE KEY UPDATE name2=values(name2)').values(data)
        self.session.execute(sql)
        self.session.commit()

    def test_model1(self):
        # 参考: https://stackoverflow.com/questions/56287070/sqlalchemy-on-duplicate-key-update
        data = [{'id': 1, "name2": 363}, {'id': 2, "name2": 3}]
        update_txt = {'id': text("values(id)"), "name2": text('values(name2)')}
        sql = insert(TestTable).values(data).on_duplicate_key_update(update_txt)
        self.session.execute(sql)
        self.session.commit()

    def test_model_best(self):
        """
        # on_duplicate_key_update  --最优
        :return:
        """
        # 参考: https://docs.sqlalchemy.org/en/14/dialects/mysql.html#insert-on-duplicate-key-update-upsert
        from sqlalchemy.dialects.mysql import insert
        data = [{'id': 1, "name2": 11}, {'id': 2, "name2": 22}]
        insert_stmt = insert(TestTable).values(data)
        # 参数赋值, 字典(inserted),   2 元组列表(inserted)
        # When rendered, the “inserted” namespace will produce the expression VALUES(<columnname>)
        on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
            id=insert_stmt.inserted.id,
            name2=insert_stmt.inserted.id
        )
        self.session.execute(on_duplicate_key_stmt)
        self.session.commit()

    def test_model3(self):
        stmt = insert(TestTable).on_duplicate_key_update({"name": "some name"})
        self.session.execute(stmt)  # [SQL: INSERT INTO test_t () VALUES () ON DUPLICATE KEY UPDATE ]
        self.session.commit()

    def tearDown(self):
        ...
        # self.session.commit()


if __name__ == '__main__':
    unittest.main()
