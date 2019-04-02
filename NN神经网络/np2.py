from numpy.random import randn  

from numpy import random  

import numpy as np  
import pandas as pd

######生成矩阵################  
# 将列表放入Numpy数组  
data = [2, 3, 4, 5]
print(data)
print(type(data))
arr = np.array(data)  
print(type(arr))
print(arr)  
# 创建二维矩阵  
data = [[1, 2, 3], [7, 8, 9]]  
arr = np.array(data)  
print(type(arr))
print(arr)  
# 输出arr的数据类型  
data = [2, 3, 4, 5]  
arr = np.array(data)  
print(arr.dtype)  
# 打印输出8*4的二维矩阵  
a = np.empty([8, 4]) 
print("a:")   
print(a)  
# 输出2*3*2的三维矩阵  
arr = np.empty([2, 3, 2])  
print(arr)  
# 输出2*4的矩阵  
a = np.empty([2, 4])  
for i in range(2):  
    a[i] = i  
print(a)  
# 输出两个2*4的矩阵  
a = np.empty([2, 4])  
for i in range(2):  
    a[i] = i  
    print(a)  
# 二维矩阵  
a = [[2, 1, 4, 6]]  
print("a1")  
print(a)  
# 输出2*2的矩阵，指定数据类型  
arr = np.array([2, 2], dtype='int32')  
print(arr)  
# 表示在【0-31】这32个数字中分成8行4列  
arr = np.arange(32).reshape((8, 4))  
print(arr)  
# 输出 0-9  
print(np.arange(10))  
# 在1和2之间（包括1和2）分成等值的3份输出，结果：[ 1.   1.5  2. ]  
print(np.linspace(1, 2, 3))  
# 输出行列都为9的单位矩阵  
print(np.eye(9))  
# 输出全为0的一维矩阵  
print(np.zeros([3]))  
# 输出均为0的4维矩阵，参数分别为维度，即第一，二，三，四维  
print(np.zeros([2, 2, 2, 2]))  
# 分别输出1.0，1.5，2.0  
for x in np.linspace(1, 2, 3):  
    print(x)  
# 输出2*4的二维矩阵  
print(np.random.rand(2, 4))  
# 2*2的矩阵  
a = np.random.rand(4).reshape(2, 2)  
print(a)  
# 输出1-10之间随机的4个整数  
print(np.random.randint(1, 10, 4))  
################索引和切片##########  
# 输出1，2  
arr = np.arange(10)  
print(arr[1:3])  
# 将第5个到第7个改为12  
arr = np.arange(10)  
arr[5:8] = 12  
print(arr)  
# 将第5个数之后全都改成10  
arr = np.arange(10)  
arr[5:] = 10  
print(arr)  
# 将arr切分成二维矩阵看，将arr[6]改成1514  
arr = np.arange(10)  
a = arr[5:8]  
a[1] = 1514  
print(arr)  
# 想一下这个是什么意思呢  
arr = np.arange(10)  
a = arr[5:8]  
a[:] = 1514  
print(arr)  
# copy和'='的区别  
arr = np.arange(10)  
print("arr:", arr)  
b = arr.copy()  
print("b.copy:", b)  
b[2] = 100  
print("after change:", b)  
print("arr:", arr)  
arr = np.arange(10)  
print("arr:", arr)  
c = arr  
print("copy", c)  
c[2] = 100  
print("after copy", c)  
print("arr:", arr)  
# copy是复制一份，而'='是视图  
# [,]和[][]是相同的  
arr = np.array([[1, 2, 3], [4, 5, 6]])  
print(arr[1, 1])  
print(arr[1][1])  
# axis 0 1  
# 0表示从行看，1表示从列看  
# 二维切片索引  
# 输出第1行  
arr = np.arange(1, 10).reshape(3, 3)  
print(arr[:1])  
# 输出2，3行  
arr = np.arange(1, 10).reshape(3, 3)  
print(arr[1:])  
# 输出第一行第一个  
arr = np.arange(1, 10).reshape(3, 3)  
print(arr[:1, :1])  
# 输出所有行和2，3列  
arr = np.arange(1, 10).reshape(3, 3)  
print(arr[:, 1:])  
# 规律：[:]指全部二维矩阵 [:2]指[0,2)的行  
print(np.zeros([3, 3]))  
print(np.zeros([10]).max())  
print(np.empty([2, 3, 2], dtype='int32').max())  
print(np.arange(9).reshape(3, 3)[:2, 1:])  
a = np.arange(12).reshape([3, 4])  
a = np.reshape(a, [4, 3])  
print(a)  
############转置############  
# 转置，相乘  
t = np.arange(9).reshape([3, 3]).T  
t1 = np.arange(1, 10, 1).reshape([3, 3])  
print(t.dot(t1))  
# 乘  
lst1 = np.array([1, 2, 3, 4])  
lst2 = np.array([10, 20, 30, 40])  
print(lst1.reshape([2, 2]))  
print(np.dot(lst1, lst2))  
# 这两个有什么区别？  
b = np.random.random([1 * 2])  # [ 0.6778996   0.29006868]  
print(b)  
b = np.random.random([1] * 2)  # [[ 0.09265586]]  
print(b)  
# reshape中的参数是维度  
ar = np.arange(16).reshape([2, 2, 4])  
print(ar)  
c = np.arange(16).reshape([2, 2, 4])  
# 三维矩阵转置  
c = np.arange(16).reshape([2, 2, 4])  
d = np.transpose(c, [1, 0, 2])  
e = c.T  
print(d)  
print(e)  
# 矩阵横向合并  
a1 = np.array([[1, 2], [3, 4]])  
a2 = np.array([[5, 6], [7, 8]])  
print(np.hstack([a1, a2]))  
# 矩阵纵向合并  
a1 = np.array([[1, 2], [3, 4]])  
a2 = np.array([[5, 6], [7, 8]])  
print(np.vstack([a1, a2]))  
###########函数###########  
# 取指数函数  
print(np.exp([3, 1]))  
# 接受两个一维数组，产生两个二维矩阵  
points = np.arange(-5, 5, 1)  
xs, ys = np.meshgrid(points, points)  
print(xs)  
print(ys)  
# #where过滤条件  
# 将正态分布a中元素大于0的改成1，小于0的改成-1  
a = randn(9).reshape([3, 3])  
print(a)  
print(np.where(a > 0, 1, -1))  
# 文件保存  
arr = np.arange(10)  
np.save('abc', arr)  
print(np.load('abc.npy'))  
a = np.arange(1, 10).reshape([3, 3])  
# 转置和逆  
a = np.arange(10)  
b = a.T  
b = np.invert(a)  # 矩阵的逆  
# 行相加，第二个等于第一个加第二个，依次类推  
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
print(a.cumsum(0))  
# 列相加，第二个等于第一个加第二个，依次类推  
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
print(a.cumsum(0))  
# 行累积  
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
print(a.cumprod(0))  
# 列累积  
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
print(a.cumprod(1))  
# 按行排序，从左到右依次增大  
arr = randn(5, 3)  
arr.sort(1)  
print(arr)  
# 随机漫步  
nsteps = 1000  
draws = np.random.randint(0, 2, size=nsteps)  
steps = np.where(draws > 0, 1, -1)  
walk = steps.cumsum()  
print(walk)  
#-----------------------------------------------------------  
