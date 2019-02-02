import numpy as np


def tanh(x):
    return np.tanh(x)


def tanh_deriv(x):
    return 1.0 - np.tanh(x) * np.tanh(x)


def logistic(x):
    return 1 / (1 + np.exp(-x))


def logistic_derivative(x):
    return x


class NeuralNetwork:

    def __init__(self, layers, activation='tanh'):
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv

        self.weights = []
        for i in range(1, len(layers) - 1):
            self.weights.append((2 * np.random.random((layers[i - 1], layers[i])) - 1) * 0.25)  # 产生矩阵
            self.weights.append((2 * np.random.random((layers[i], layers[i + 1])) - 1) * 0.25)  # 产生矩阵

        self.deviation = []
        for i in range(1, len(layers)):
            self.deviation.append((2 * np.random.random(layers[i]) - 1) * 0.25)  # 产生矩阵

    def fit(self, X, y, learning_rate=0.2, epochs=10000):
        # --X二维的,一行代表一个实例  Y 输出值  learning_rate 学习率,, epochs,避免计算量大,使用抽样数据,终止三条件之一,循环次数
        X = np.atleast_2d(X)  # 彩色 可能三维
        y = np.array(y)

        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            output = [X[i]]
            for j in range(len(self.weights)):
                output.append(self.activation(np.dot(output[j], self.weights[j]) + self.deviation[j]))  # 添加的是矩阵

            err = y[i] - output[-1]
            error = [output[-1] * (1 - output[-1]) * err]  # 误差 list
            # --deltas = [error * self.activation_deriv(a[-1])] #For output layer, Err calculation (delta is updated error)

            # Staring backprobagation
            length = len(self.weights)
            length2 = len(output)
            for j in range(length - 1):
                error.append((error[j].dot(self.weights[length - j - 1].T)) * output[length2 - j - 2] * (
                        1 - output[length2 - j - 2]))
            error.reverse()  # reverse 颠倒顺序
            for j in range(len(self.weights)):  # 权重 偏向更新
                self.weights[j] += np.array([output[j]]).T.dot(np.array([error[j]])) * learning_rate
                self.deviation[j] += learning_rate * error[j]

    def predict(self, X):  # 测试的实例  list
        X = np.atleast_2d(X)
        X = np.array(X)
        result = X
        for i in range(0, len(self.weights)):
            result = self.activation(np.dot(result, self.weights[i]) + self.deviation[i])
        return result

# print(NeuralNetwork([3, 2, 1], "tanh").weights[0], "hhhhhhhhhhhh")
