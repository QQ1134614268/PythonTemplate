from NN神经网络 import NeuralNetwork
import numpy as np

nn = NeuralNetwork.NeuralNetwork([2, 2, 1], 'tanh') # 1.如果EX.py 中有Class example()，要调用改函数中的方法，方法是：模块名.类名.方法名
# 2.如果调用的是EX.py文件中的def example()函数：模块名.函数名
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
print(X)
# [[0 0]
#  [0 1]
#  [1 0]
#  [1 1]]
print(y)
# X = [[0, 0], [0, 1], [1, 0], [1, 1]]
# print(X)
# [[0, 0], [0, 1], [1, 0], [1, 1]]
nn.fit(X, y)
for i in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    print(i, nn.predict(i))