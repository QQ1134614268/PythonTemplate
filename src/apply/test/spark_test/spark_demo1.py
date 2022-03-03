# -*- coding:utf-8 -*-
"""
@Time: 2022/3/3
@Description:
"""
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("spark0401")
    sc = SparkContext(conf=conf)
    '''
    map:
        map(func)
        将func函数作用到数据集的每个元素上，生成一个新的分布式数据集返回
    '''
    print("***************************map***************************")


    def my_map():
        # 创建一个序列
        data = [1, 2, 3, 4, 5]
        # 将序列转换为RDD
        rdd1 = sc.parallelize(data)
        # 使用函数对RDD进行作用，生成RDD2
        rdd2 = rdd1.map(lambda x: x * 2)
        # 使用collect()讲结果输出
        print(rdd2.collect())


    my_map()


    def my_map2():
        a = sc.parallelize(["dog", "tiger", "lion", "cat", "panter", "eagle"])
        b = a.map(lambda x: (x, 1))  # 进来一个x，返回一个(x,1)的形式
        print(b.collect())


    my_map2()
    print("***************************filter***************************")


    def my_filter():
        # 给一个数据
        data = [1, 2, 3, 4, 5]
        rdd1 = sc.parallelize(data)
        mapRdd = rdd1.map(lambda x: x ** 2)
        filterRdd = mapRdd.filter(lambda x: x > 5)
        print(filterRdd.collect())


    '''
    filter:
        filter(func)
        返回所有func返回值为true的元素，生成一个新的分布式数据集返回
    '''


    def my_filter():
        data = [1, 2, 3, 4, 5]
        rdd1 = sc.parallelize(data)
        mapRdd = rdd1.map(lambda x: x * 2)
        filterRdd = mapRdd.filter(lambda x: x > 5)
        print(filterRdd.collect())
        print(sc.parallelize(data).map(lambda x: x * 2).filter(lambda x: x > 5).collect())


    my_filter()
    print("***************************flatMap()***************************")


    # Wordcount第一步：
    def my_flatMap():
        # flatMap,将东西压扁/拆开 后做map
        data = ["hello spark", "hello world", "hello world"]
        rdd = sc.parallelize(data)
        print(rdd.flatMap(lambda line: line.split(" ")).collect())


    my_flatMap()
    print("***************************groupBy()***************************")


    def my_groupBy():
        data = ["hello spark", "hello world", "hello world"]
        rdd = sc.parallelize(data)
        mapRdd = rdd.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1))
        groupByRdd = mapRdd.groupByKey()
        print(groupByRdd.collect())
        print(groupByRdd.map(lambda x: {x[0]: list(x[1])}).collect())


    my_groupBy()

    print("***************************reduceByKey()***************************")


    # 出现Wordcount结果
    def my_reduceByKey():
        data = ["hello spark", "hello world", "hello world"]
        rdd = sc.parallelize(data)
        mapRdd = rdd.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1))
        reduceByKeyRdd = mapRdd.reduceByKey(lambda a, b: a + b)
        print(reduceByKeyRdd.collect())


    my_reduceByKey()

    print("***************************sortByKey()***************************")


    # 将Wordcount结果中数字出现的次数进行降序排列
    def my_sort():
        data = ["hello spark", "hello world", "hello world"]
        rdd = sc.parallelize(data)
        mapRdd = rdd.flatMap(lambda line: line.split(" ")).map(lambda x: (x, 1))
        reduceByKeyRdd = mapRdd.reduceByKey(lambda a, b: a + b)
        # reduceByKeyRdd.sortByKey().collect() 此时是按照字典在排序
        # reduceByKeyRdd.sortByKey(False).collect()
        # 先对对键与值互换位置，再排序，再换位置回来
        reduceByKey = reduceByKeyRdd.map(lambda x: (x[1], x[0])).sortByKey(False).map(lambda x: (x[1], x[0])).collect()
        print(reduceByKey)


    my_sort()

    print("***************************union()***************************")


    def my_union():
        a = sc.parallelize([1, 2, 3])
        b = sc.parallelize([3, 4, 5])
        U = a.union(b).collect()
        print(U)


    my_union()

    print("***************************union_distinct()***************************")


    def my_distinct():
        # 这个和数学并集一样了
        a = sc.parallelize([1, 2, 3])
        b = sc.parallelize([3, 4, 2])
        D = a.union(b).distinct().collect()
        print(D)


    my_distinct()

    print("***************************join()***************************")


    def my_join():
        a = sc.parallelize([("A", "a1"), ("C", "c1"), ("D", "d1"), ("F", "f1"), ("F", "f2")])
        b = sc.parallelize([("A", "a2"), ("C", "c2"), ("C", "c3"), ("E", "e1")])
        J = a.fullOuterJoin(b).collect
        print(J)


    my_join()

    sc.stop()

'''
Spark Core核心算子回顾
 -- Transformation算子编程：
   map、filter、groupByKey、flatMap、reduceByKey、sortByKey、join等
'''
