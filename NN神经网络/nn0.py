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

        self.weights = []  # 权重
        for i in range(1, len(layers) - 1):  # 初始化权重
            self.weights.append((2 * np.random.random((layers[i - 1]  , layers[i])) - 1) * 0.25)  # 产生矩阵
            self.weights.append((2 * np.random.random((layers[i]  , layers[i + 1])) - 1) * 0.25)  # 产生矩阵

        self.deviation = []
        for i in range(1, len(layers)):
            self.deviation.append((2 * np.random.random((1, layers[i])) - 1) * 0.25)  # 产生矩阵

    def fit(self, X, y, learning_rate=0.2, epochs=10000):
        # --X二维的,一行代表一个实例  Y 输出值  learning_rate 学习率,, epochs,避免计算量大,使用抽样数据,终止三条件之一,循环次数
        X = np.atleast_2d(X)  # 彩色 可能三维
        temp = np.ones([X.shape[0], X.shape[1]])  # X.shape[0]
        temp[:, :] = X  # 添加 偏差??
        X = temp
        y = np.array(y)

        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            for j in range(len(self.weights)):  # going forward network, for each layer
                out = np.dot(a[j], self.weights[j]) + self.deviation[j]
                a.append(self.activation(out))  # dot 内积

            # error = y[i] - a[-1]  #  y[i]???
            # error = a[-1]*(1-a[-1])*(y[i]-a[-1]) # 目标层
            error = y[i] - a[-1]
            deltas = [a[-1] * (1 - a[-1]) * error]
            # Staring backprobagation
            length = len(self.weights)
            length2 = len(a)
            for j in range(length):  #
                # Compute the updated error (i,e, deltas) for each node going from top layer to input layer
                deltas.append((deltas[j].dot(self.weights[length - j - 1].T)) * self.activation_deriv(a[length2 - j - 2]) * (1 - self.activation_deriv(a[length2 - j - 2])))
                # deltas.append(  deltas[-1].dot(self.weights[j].T) * self.activation_deriv(a[j]))  # 往回走使用反函数activation_deriv
            deltas.reverse()  # reverse 颠倒顺序
            for i in range(len(self.weights)):
                # layer = np.atleast_2d(a[i+1])
                aaa = np.array(a[i + 1])
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
