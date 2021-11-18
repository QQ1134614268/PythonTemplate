import unittest

import pymongo


class Es(unittest.TestCase):
    def setUp(self) -> None:
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')

    def test_main(self):
        db = self.client.mydemo
        collection = db["students"]
        student = {'id': '20170101', 'name': '小明', 'age': 22, 'gender': '男性'}
        # 插入 insert_one insert_many
        result = collection.insert(student)

        query_filter = {'name': 'Mike'}
        student = collection.find_one(query_filter)
        student['age'] = 25
        # 更新 update_one update_many
        result = collection.update(query_filter, {'$set': student})

        # 查找
        results = db.collection.find()
        results = collection.find({"name": {"$regex": "^M.*"}})
        results = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(1)
        # 删除
        result = collection.remove({'name': 'Jordan'})
        result = collection.delete_one({'name': 'Kevin'})
        result = collection.delete_many({'name': 'Kevin'})

    def tear_down(self):
        self.es.close()
