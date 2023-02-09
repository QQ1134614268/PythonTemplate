# -*- coding:utf-8 -*-
"""
@Time: 2022/3/3
@Description:
"""
import unittest

from pyspark import SparkConf, SparkContext


class TestSpark(unittest.TestCase):  # 安装spark后运行
    """
    Spark Core核心算子回顾
     -- Transformation算子编程：
       map、filter、groupByKey、flatMap、reduceByKey、sortByKey、join等
    """

    def setUp(self):
        conf = SparkConf().setMaster("local[2]").setAppName("spark0401")
        self.sc = SparkContext(conf=conf)

    def tearDown(self):
        self.sc.stop()

    def test_my_map(self):
        # 创建一个序列
        data = [1, 2, 3, 4, 5]
        # 将序列转换为RDD
        rdd1 = self.sc.parallelize(data)
        # 使用函数对RDD进行作用，生成RDD2
        rdd2 = rdd1.map(lambda x: x * 2)
        # 使用collect()讲结果输出
        print(rdd2.collect())

    def test_my_map2(self):
        a = self.sc.parallelize(["dog", "tiger", "lion", "cat", "panter", "eagle"])
        b = a.map(lambda x: (x, 1))  # 进来一个x，返回一个(x,1)的形式
        print(b.collect())

    def test_my_filter(self):
        # 给一个数据
        data = [1, 2, 3, 4, 5]
        rdd1 = self.sc.parallelize(data)
        map_rdd = rdd1.map(lambda x: x ** 2)
        filter_rdd = map_rdd.filter(lambda x: x > 5)
        print(filter_rdd.collect())

    def test_my_filter2(self):
        data = [1, 2, 3, 4, 5]
        rdd1 = self.sc.parallelize(data)
        map_rdd = rdd1.map(lambda x: x * 2)
        filter_rdd = map_rdd.filter(lambda x: x > 5)
        print(filter_rdd.collect())
        print(self.sc.parallelize(data).map(lambda x: x * 2).filter(lambda x: x > 5).collect())

    def test_my_flatMap(self):
        # flatMap,将东西压扁/拆开 后做map
        data = ["hello spark", "hello world", "hello world"]
        rdd = self.sc.parallelize(data)
        print(rdd.flatMap(lambda line: line.split(" ")).collect())

    def test_my_groupBy(self):
        data = ["hello spark", "hello world", "hello world"]
        rdd = self.sc.parallelize(data)
        map_rdd = rdd.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1))
        group_by_rdd = map_rdd.groupByKey()
        print(group_by_rdd.collect())
        print(group_by_rdd.map(lambda x: {x[0]: list(x[1])}).collect())

    # 出现Wordcount结果
    def test_my_reduceByKey(self):
        data = ["hello spark", "hello world", "hello world"]
        rdd = self.sc.parallelize(data)
        map_rdd = rdd.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1))
        reduce_by_key_rdd = map_rdd.reduceByKey(lambda a, b: a + b)
        print(reduce_by_key_rdd.collect())

    def test_my_sort(self):
        data = ["hello spark", "hello world", "hello world"]
        rdd = self.sc.parallelize(data)
        map_rdd = rdd.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1))
        reduce_by_key_rdd = map_rdd.reduceByKey(lambda a, b: a + b)
        # reduce_by_key_rdd.sortByKey().collect() 此时是按照字典在排序
        # reduce_by_key_rdd.sortByKey(False).collect()
        # 先对对键与值互换位置，再排序，再换位置回来
        reduce_by_key = reduce_by_key_rdd.map(lambda x: (x[1], x[0])).sortByKey(False).map(
            lambda x: (x[1], x[0])).collect()
        print(reduce_by_key)

    def test_my_union(self):
        data1 = self.sc.parallelize([1, 2, 3])
        data2 = self.sc.parallelize([3, 4, 5])
        spark_union = data1.union(data2).collect()
        print(spark_union)

    def test_my_distinct(self):
        # 这个和数学并集一样了
        data1 = self.sc.parallelize([1, 2, 3])
        data2 = self.sc.parallelize([3, 4, 2])
        spark_distinct = data1.union(data2).distinct().collect()
        print(spark_distinct)

    def test_my_join(self):
        data1 = self.sc.parallelize([("A", "a1"), ("C", "c1"), ("D", "d1"), ("F", "f1"), ("F", "f2")])
        data2 = self.sc.parallelize([("A", "a2"), ("C", "c2"), ("C", "c3"), ("E", "e1")])
        spark_full_out_join = data1.fullOuterJoin(data2).collect
        print(spark_full_out_join)

    def test_my_action(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        rdd = self.sc.parallelize(data)
        rdd.collect()
        rdd.count()
        rdd.take(3)  # 取前三个
        rdd.max()  # 最大值
        rdd.min()  # 最小值
        rdd.sum()  # 求和
        rdd.reduce(lambda x, y: x + y)  # 相邻两个相加
        rdd.foreach(lambda x: print(x))
