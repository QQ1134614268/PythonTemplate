import unittest

import pymongo


class TestMongodb(unittest.TestCase):
    def setUp(self) -> None:
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')

    def test_main(self):
        db = self.client["test"]
        student_table = db["student"]
        student = {'id': '20170101', 'name': '小明', 'age': 22, 'gender': '男性'}
        # 插入 insert_one insert_many
        result = student_table.insert(student)
        print(result)

        query_filter = {'name': '小明'}
        student = student_table.find_one(query_filter)
        student['age'] = 25
        # 更新 update_one update_many
        result = student_table.update(query_filter, {'$set': student})
        print(result)

        # 查找
        result = list(student_table.find())
        print(result)
        result = list(student_table.find({"name": {"$regex": "^小.*"}}))
        print(result)
        result = list(student_table.find().sort('name', pymongo.ASCENDING).skip(0).limit(10))
        print(result)

        # 删除
        result = student_table.remove({'name': 'Jordan'})
        print(result)
        result = student_table.delete_one({'name': 'Kevin'})
        print(result)
        result = student_table.delete_many({'name': 'Kevin'})
        print(result)
