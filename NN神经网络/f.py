import numpy as np


def tanh(x):
    return np.tanh(x)


def tanh_deriv(x):
    return 1.0 - np.tanh(x) * np.tanh(x)

 
def logistic(x):
    return 1 / (1 + np.exp(-x))


def logistic_derivative(x):
    return logistic(x) * (1 - logistic(x))


class NeuralNetwork:

    def __init__(self, layers, activation='tanh'):
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv

        self.weights = []  # 权重 list
        for i in range(len(layers) - 1):  # 初始化权重
            self.weights.append(np.random.random((layers[i]  , layers[i + 1])))  # 产生矩阵

        self.deviation = []
        for i in range(len(layers) - 1):
            self.deviation.append(np.random.random((layers[i + 1])))  # 产生矩阵

    def fit(self, X, y, learning_rate=0.2, epochs=10000):  # X二维的,一行代表一个实例  Y 输出值
        #  learning_rate 学习率,, epochs,避免计算量大,使用抽样数据,终止三条件之一,循环次数
        temp = np.ones([X.shape[0], X.shape[1] + 1])         
        temp[:, :] = X  # 添加 偏差??
        X = temp
        y = np.array(y)

        for k in range(epochs):
            i = np.random.randint(X.shape[0])  # 从X中选取任一行
            outList = []  # 输出集
            outList.append(X[i])  # 入参当做第一个输出集
            for j in range(len(self.weights)):  # going forward network, for each layer
                out = np.dot(outList[j], self.weights[j]) + self.deviation[j]
                outList.append(self.activation(out)) 

#             out = outList[-1]
            deltas = [outList[-1] * (1 - outList[-1]) * (y[i] - outList[-1])]  # 输出层误差集合   为什么这么计算误差 TODO
            length = len(self.weights)
            length2 = len(outList)
            for j in range(length):  #
                temp = outList[j].dot(1 - outList[j]).dot(deltas[j].dot(self.weights[length - j - 1].T))
                deltas.append(temp)
#                 deltas.append((deltas[j].dot(self.weights[length - j - 1].T)) * self.activation_deriv(outList[length2 - j - 2]) * (1 - self.activation_deriv(outList[length2 - j - 2])))
                # deltas.append(  deltas[-1].dot(self.weights[j].T) * self.activation_deriv(a[j]))  # 往回走使用反函数activation_deriv
            deltas.reverse()  # reverse 颠倒顺序
            for i in range(len(self.weights)):
                # layer = np.atleast_2d(a[i+1])
                aaa = np.array(outList[i + 1])
                bbb = np.array(deltas[i])
                # delta = np.atleast_2d(deltas[i])
                # self.weights[i] += learning_rate * layer.T.dot(delta)  # T  转置
                self.weights[i] += bbb.T.dot(aaa) * learning_rate  # T  转置

                # 偏向更新
                self.deviation[i] += learning_rate * deltas[i + 1]

    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0])
        temp[:] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a


# print(NeuralNetwork([3,2,1], "tanh").weights[0],NeuralNetwork([3,2,1], "tanh").weights[1])
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    """sigmoid函数的导数"""
    return sigmoid(z) * (1 - sigmoid(z)) 

