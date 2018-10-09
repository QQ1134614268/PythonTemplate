
import  numpy as np
import random

# def sigmoid(x):


class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]  # zip ???
        # np.random.rand(y, 1): 随机从正态分布(均值0, 方差1) 中生成

    def feedforward(self, a):
        """Return the output of the network if "a" is input."""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a
    def SDG(self):
        pass


net= Network([2,3,1])
print(net.num_layers)
print(net.sizes)
print(net.biases)
print(net.weights)