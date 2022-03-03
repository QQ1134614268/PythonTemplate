# -*- coding:utf-8 -*-
"""
@Time: 2022/3/3
@Description:
"""
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("spark0401")
    sc = SparkContext(conf=conf)


    def my_action():
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        rdd = sc.parallelize(data)
        rdd.collect()
        rdd.count()
        rdd.take(3)  # 取前三个
        rdd.max()  # 最大值
        rdd.min()  # 最小值
        rdd.sum()  # 求和
        rdd.reduce(lambda x, y: x + y)  # 相邻两个相加
        rdd.foreach(lambda x: print(x))


    my_action()
    sc.stop()
