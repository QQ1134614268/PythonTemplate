import unittest

import pymongo


class Es(unittest.TestCase):
    def setUp(self) -> None:
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')

    def test_main(self):
        db = self.client["test"]
        student_table = db["student"]
        student = {'id': '20170101', 'name': '小明', 'age': 22, 'gender': '男性'}
        # 插入 insert_one insert_many
        result = student_table.insert(student)

        query_filter = {'name': '小明'}
        student = student_table.find_one(query_filter)
        student['age'] = 25
        # 更新 update_one update_many
        result = student_table.update(query_filter, {'$set': student})

        # 查找
        results = list(student_table.find())
        results = list(student_table.find({"name": {"$regex": "^小.*"}}))
        results = list(student_table.find().sort('name', pymongo.ASCENDING).skip(0).limit(10))

        # 删除
        result = student_table.remove({'name': 'Jordan'})
        result = student_table.delete_one({'name': 'Kevin'})
        result = student_table.delete_many({'name': 'Kevin'})

    def tear_down(self):
        self.es.close()
