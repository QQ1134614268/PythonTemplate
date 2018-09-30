'''
Created on 2018年5月14日

@author: Administrator
'''
import math
import random

network = [4, [16], 1]  # 神经网络3层, 1个隐藏层; 4个input和1个output

population = 50  # 遗传算法相关
elitism = 0.2
random_behaviour = 0.1
mutation_rate = 0.5
mutation_range = 2
historic = 0
low_historic = False
score_sort = -1
n_child = 1


# 激活函数  
def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


# random number  
def random_clamped():
    return random.random() * 2 - 1


# "神经元"  
class Neuron():
    def __init__(self):  # 权重,偏向 默认偏向为 0
        self.biase = 0
        self.weights = []

    def init_weights(self, n):  # 本神经元 与上一层神经元  产生 权重 参数
        self.weights = []
        for i in range(n):
            self.weights.append(random_clamped())

    def __repr__(self):
        return 'Neuron weight size:{}  biase value:{}'.format(len(self.weights), self.biase)


class Layer():  # 层   index  neurons 神经元
    def __init__(self, index):
        self.index = index
        self.neurons = []

    def init_neurons(self, n_neuron, n_input):  # 该层有多少神经元个数,前一层有多少神经元,添加神经元,并初始化其权重参数
        self.neurons = []
        for i in range(n_neuron):
            neuron = Neuron()
            neuron.init_weights(n_input)
            self.neurons.append(neuron)

    def __repr__(self):
        return 'Layer ID:{}  Layer neuron size:{}'.format(self.index, len(self.neurons))


class NeuroNetwork():  # 网络
    def __init__(self):
        self.layers = []

    def init_neuro_network(self, input, hiddens,
                           output):  # 本network = [4, [16], 1],,input:输入层神经元数 hiddens:隐藏层 output:输出层神经元数

        # 第0层 (输入层) 特殊处理

        index = 0  # 首先 index=0,第0层神经元,
        previous_neurons = 0  # 前一层神经元
        # input
        layer = Layer(index)  # 第0层神经元,
        layer.init_neurons(input, previous_neurons)  # 第0层神经元,有input 个神经元,前一层没有神经元
        previous_neurons = input  # 令 前一层神经元个数  为 input个
        self.layers.append(layer)  # 网络 添加第0层神经元,,
        index += 1  # 第1 层

        # 隐藏层
        for i in range(len(hiddens)):  # hiddens list数据结构,代表每层神经元个数
            layer = Layer(index)  # 标记本层处于神经网络 i 层
            layer.init_neurons(hiddens[i], previous_neurons)  # 第 i 层神经元,有  hiddens[i] 个神经元,前一层 previous_neurons个神经元
            previous_neurons = hiddens[i]
            self.layers.append(layer)
            index += 1

        # 输出层
        layer = Layer(index)  # 该层 处于神经网络 层级,,
        layer.init_neurons(output, previous_neurons)  # 初始化,,该层神经元个数,上一层神经元个数,,一遍初始化权重参数
        self.layers.append(layer)  # 神经网络 添加 输出层

    def get_weights(self):  # 获取权重
        data = {'network': [], 'weights': []}
        for layer in self.layers:  # 遍历 神经网络 每层(每层神经元)
            data['network'].append(len(layer.neurons))  # 添加 每层神经元个数  ,  从输入层 到输出层的个数
            for neuron in layer.neurons:  # 遍历每层的每个神经元
                for weight in neuron.weights:  # 添加  权重 ,,每个神经元权重,,
                    data['weights'].append(weight)
        return data

    def set_weights(self, data):  # 设置 权重
        previous_neurons = 0
        index = 0
        index_weights = 0

        self.layers = []
        for i in data['network']:  # data['network'] =[4,16,...,1]  第一层 4个,第二层 16个,,,....
            layer = Layer(index)  # 标记层级  i
            layer.init_neurons(i, previous_neurons)  # 每层初始化神经元个数
            for j in range(len(layer.neurons)):  # 遍历神经层,,  for j in range(4)
                for k in range(len(layer.neurons[j].weights)):  # 遍历   本层 第j个神经元权重(list)长度
                    layer.neurons[j].weights[k] = data['weights'][index_weights]  # 本层 第j个神经元 第K权重=data['weights'][0]
                    index_weights += 1
            previous_neurons = i  # 前一层神经元 个数
            index += 1  # 标记层级 (i)  +1
            self.layers.append(layer)  # 神经网络添加神经元 层

    # set_weights 把 data中数据设置成网络的数据,,,,get_weights 读取网络数据,塞进data中

    # 输入游戏环境中的一些条件(如敌机位置), 返回要执行的操作
    def feed_forward(self, inputs):  # 输入参数--??
        for i in range(len(inputs)):  # 第0层(输入层)每个神经元偏向设为 inputs[i]
            self.layers[0].neurons[i].biase = inputs[i]

        prev_layer = self.layers[0]  # 初始化 前一层为输入层
        for i in range(len(self.layers)):  # 遍历网络 的 每层
            if i == 0:  # 第一层没有weights  ,没有操作
                continue
            for j in range(len(self.layers[i].neurons)):  # 每层  每个神经元
                sum = 0
                for k in range(len(prev_layer.neurons)):  # 遍历前一层神经元个数,  求和 == 前一层神经元偏向*本层神经元第K个权重,,
                    sum += prev_layer.neurons[k].biase * self.layers[i].neurons[j].weights[k]
                    self.layers[i].neurons[j].biase = sigmoid(sum)  # 更新 本层 偏向
            prev_layer = self.layers[i]  # prev_layer 更新

        out = []
        last_layer = self.layers[-1]
        for i in range(len(last_layer.neurons)):
            out.append(last_layer.neurons[i].biase)
        return out  # 返回 输出 结果

    def print_info(self):
        for layer in self.layers:
            print(layer)


class Genome():  # "基因组" (每个个体)   ,,  分数 -- 神经网络权重
    def __init__(self, score, network_weights):
        self.score = score  # 分数
        self.network_weights = network_weights  # 权重


class Generation():  # 新个体??,,
    def __init__(self):
        self.genomes = []  #

    def add_genome(self, genome):  # 添加个体
        i = 0
        for i in range(len(self.genomes)):  # 遍历产生个体个数  ,,
            if score_sort < 0:  # 全局变量   score_sort = -1  ,,
                if genome.score > self.genomes[i].score:  # score_sort  如果添加个体得分  > genomes[i],,,退出 - - 遍历产生个体个数
                    break
            else:
                if genome.score < self.genomes[i].score:  # score_sort  如果添加个体得分  > genomes[i],,,退出 - - 遍历产生个体个数
                    break
        self.genomes.insert(i, genome)  # 将个体插入第i位置

    def breed(self, genome1, genome2, n_child):  # 杂交+突变
        datas = []
        for n in range(n_child):
            data = genome1  # data 等于 网络genome1
            for i in range(len(genome2.network_weights['weights'])):  # 遍历 网络 genome2 的权重个数
                if random.random() <= 0.5:  # 若随机数小于 0.5
                    data.network_weights['weights'][i] = genome2.network_weights['weights'][i]  # 权重更新为 网络的第i个权重值

            for i in range(len(data.network_weights['weights'])):  # 遍历 网络 data 的权重个数
                if random.random() <= mutation_rate:  # 若随机数小于 mutation_rate (mutation_rate =0.5,全局变量 )
                    # data的第i权重值 更新为 随机数*mutation_range(全局变量,0.5)-mutation_range(全局变量 2)
                    data.network_weights['weights'][i] += random.random() * mutation_range * 2 - mutation_range
            datas.append(data)
        return datas  # 返回n_child个  网络

    def generate_next_generation(self):  # 生成下一代
        nexts = []
        for i in range(round(elitism * population)):  # 遍历 elitism(全局变量,0.2)*population(全局变量,50),,向上取整 ; 10个
            if len(nexts) < population:  # 如果 下一代个数小于 population(全局变量,50)
                nexts.append(self.genomes[i].network_weights)  # 添加 genomes[i]网络,,知道下一代为10个

        for i in range(
                round(random_behaviour * population)):  # 遍历 random_behaviour(全局变量,0.1)*population(全局变量,50),,向上取整;;5个
            n = self.genomes[0].network_weights  # 网络 genomes[0] 权重
            for k in range(len(n['weights'])):  # 遍历  genomes[0] 权重 个数,,
                n['weights'][k] = random_clamped()  # 用随机函数 random_clamped产生随机值,赋值给genomes[0] 权重第 K值
            if len(nexts) < population:  # 如果nexts 长度<population(全局变量,50)
                nexts.append(n)  # 添加 新网络

        max_n = 0
        while True:
            for i in range(max_n):  # 遍历
                # 孩子,,参数为genomes[i]和 genomes[max_n];n_child(全局变量,1)# 杂交+突变
                childs = self.breed(self.genomes[i], self.genomes[max_n], n_child if n_child > 0 else 1)
                for c in range(len(childs)):  # 遍历孩子个数
                    nexts.append(childs[c].network_weights)  # 将孩子添加入下一代
                    if len(nexts) >= population:  # 如果下一代个数大于population 返回下一代
                        return nexts
            max_n += 1  # 否则max_n+1
            if max_n >= len(self.genomes) - 1:  # 如果max_n> genomes长度,赋值为0, 重新开始
                max_n = 0


class Generations():
    def __init__(self):
        self.generations = []

    def first_generation(self):  # 第一代 基因组
        out = []  # 输出
        for i in range(population):  # population(全局变量,50)
            nn = NeuroNetwork()  # 神经网络
            nn.init_neuro_network(network[0], network[1], network[2])  # 初始化神经网络,,network = [4, [16], 1]
            out.append(nn.get_weights())  # 获得50个网络的权重值
        self.generations.append(Generation())  # 将 一代添加到 generations
        return out

    def next_generation(self):
        if len(self.generations) == 0:
            return False

        gen = self.generations[-1].generate_next_generation()  # generations倒数第一个的50个网络的权重值
        self.generations.append(Generation())  # 将 一代添加到 generations
        return gen

    def add_genome(self, genome):  # 添加新个体(网络)
        if len(self.generations) == 0:
            return False

        return self.generations[-1].add_genome(genome)


class NeuroEvolution():  # 进化网络
    def __init__(self):
        self.generations = Generations()  # 产生Generations网络

    def restart(self):
        self.generations = Generations()  # 重新产生

    def next_generation(self):  # 下一次  遗传
        networks = []
        if len(self.generations.generations) == 0:  # 下一次  遗传的个数为0
            networks = self.generations.first_generation()  # 产生第一代
        else:
            networks = self.generations.next_generation()  # 产生下一代

        nn = []
        for i in range(len(networks)):  # 遍历networks 个数
            n = NeuroNetwork()  #
            n.set_weights(networks[i])  # 将networks[i] 赋值给 n 这个网络
            nn.append(n)  # 网络集合  添加新网络

        if low_historic:  # low_historic(全局变量,False )
            if len(self.generations.generations) >= 2:  # 如果 ..
                genomes = self.generations.generations[len(self.generations.generations) - 2].genomes
                for i in range(genomes):
                    genomes[i].network = None

        if historic != -1:  # historic(全局变量,0)
            if len(self.generations.generations) > historic + 1:  # 进化网络的长度>historic(全局变量,0) + 1
                del self.generations.generations[
                    0:len(self.generations.generations) - (historic + 1)]  # 删除 从第0 至 (第进化网络长度- (historic + 1))

        return nn  # 返回网络的集合

    def network_score(self, score, network):  # 网络的 得分
        self.generations.add_genome(Genome(score, network.get_weights()))  # 进化网络添加 ,
