print("*********this*is*init***************")

for i in range(1, 0):  # 左包含右不包含
    print(i)

import numpy as np

t= np.random.random(5)
print("ttttttt ",t)

x = [[1, 2, 3, 4], [1, 2, 3, 4]]  # list 结构
# a = [x[0]]
# print(a)

# print(a.T)
print(np.ones([2, 2]))  # 产生矩阵数组
x = np.array(x)  # 数组结构
t = x.shape  # (m,n) tuple 元组,,数组
print(t)
t0 = t[0]  # =m
tr = (88888, 2, 3)
print(tr[0])

print(len(x))
zhuan = x.T  # T  矩阵转置
dott = zhuan.dot(x)  # 内积
print(zhuan.dot(x))  # tuple
print(np.dot(zhuan, x))
print(np.dot(zhuan, x) == zhuan.dot(x))
# temp[:, 0:-1]
x[:, 0:-1] = 0
print(x)

# print(np.dot(zhuan, zhuan))
l = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]
A = np.array(l)
print(A)
ll = [1, 2, 3]
AA = np.array(ll)
print(AA)
print(A.dot(AA))


import numpy
a=[[1,2,3]]
b=[[1,2,3]]
print(a[0],"ssssssssss")
a=numpy.array(a)
b=numpy.array(b)
# print(a*b)
# print(1-a)
# print(a.dot(b))
print(a.T.dot(b))

print(a[0])

