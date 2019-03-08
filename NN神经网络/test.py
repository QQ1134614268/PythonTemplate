import numpy as np
wights = []
x = np.random.random(4)
print(x)
print(type(x))
wights.append(x)
wights.append(x)
print(wights)
print(type(wights))

x = np.random.random((3, 2))
print(x)

layes = [3, 2, 1]
for i in range(1, len(layes) - 1):  # 初始化权重
    print(i)
print(layes[0])
x = np.ones([3, 4])
print(type(x))

x = np.array([[1, 2], [1, 2], [1, 2]])
print(1 - x)
shape = x.shape
print(type(shape), " ", x.shape)
print(shape[0])
y = x[1]
y1 = np.array([[1, 1, 1], [1, 1, 1]])
z = np.dot(y, y1)  
print("--", z)
# np.dot(a[j], self.weights[j]) + self.deviation[j]
print(y, type(y))

x = np.ones((2, 4))
print(x)

