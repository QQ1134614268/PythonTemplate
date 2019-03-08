# coding=utf-8

"""RNN-LSTM卷积神经网络实现mnist"""
# 读取数据

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
train_imgs = mnist.train.images
train_labs = mnist.train.labels
test_imgs = mnist.test.images
test_labs = mnist.test.labels

num_train = train_imgs.shape[0]  # 训练集个数
num_test = test_imgs.shape[0]  # 测试集个数
dim = train_imgs.shape[1]  # 单张图片维度28*28
num_classes = train_labs.shape[1]  # 类别

# 定义网络维度
dim_input = 28  # 输入为1*28
dim_hidden = 128  # 隐层维度为128
dim_output = num_classes  # 输出维度1*10
num_steps = 28  # 将一张图拆成28个1*28输入

# 定义数据集输入以及ground truth
x_data = tf.placeholder(tf.float32, [None, num_steps, dim_input])  # 样本个数不确定，所以为None
y_real = tf.placeholder(tf.float32, [None, dim_output])

# 权重参数
stddev = 0.1
weights = {"hidden": tf.Variable(tf.random_normal([dim_input, dim_hidden], stddev=stddev)),
           "out": tf.Variable(tf.random_normal([dim_hidden, dim_output], stddev=stddev))}
biases = {"hidden": tf.Variable(tf.zeros([dim_hidden])), "out": tf.Variable(tf.zeros([dim_output]))}


def RNN_network(_X, _W, _b, _num_steps, _name):
    """
    RNN-lstm 网络结构
    :param _X:
    :param _W:
    :param _b:
    :param _num_steps:
    :param _name:
    :return:
    """
    # 1. 对输入进行转换
    # -1.1 将[batch_size, num_steps, dim_input]转换成[num_steps, batch_size, dim_input]
    _X = tf.transpose(_X, perm=[1, 0, 2])
    # -1.2 再将[num_steps, batch_size, dim_input]转换成[num_steps*batch_size, dim_input]
    _X = tf.reshape(_X, [-1, dim_input])

    # 2. 通过隐层
    _H = tf.add(tf.matmul(_X, _W["hidden"]), _b["hidden"])

    # 3. 隐层输出进行切分
    _H_split = tf.split(value=_H, num_or_size_splits=num_steps, axis=0)

    # 4. 获得LSTM的输出(LSTM_0)和状态(LSTM_S)
    with tf.variable_scope(_name, reuse=tf.AUTO_REUSE):  # 指定scope
        lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(dim_hidden, forget_bias=1.0)
        _LSTM_0, _LSTM_S = tf.nn.static_rnn(lstm_cell, _H_split, dtype=tf.float32)

    # 5. 输出
    _O = tf.add(tf.matmul(_LSTM_0[-1], _W["out"]), _b["out"])  # 取最后一个_LSTM_0经过神经元

    return {"X": _X, "H": _H, "H_split": _H_split, "LSTM_0": _LSTM_0, "LSTM_S": _LSTM_S, "OUT": _O}


y_pred = RNN_network(x_data, weights, biases, num_steps, "basic")["OUT"]

# 定义loss函数以及优化器
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_pred, labels=y_real))
op = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

# 定义准确率
correct = tf.equal(tf.arg_max(y_pred, 1), tf.arg_max(y_real, 1))  # 计算出预测值与真实值是否相等(独热码为1的索引是否相等)
accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))  # 每个batch的平均准确率 将True转成float

# 训练参数
training_epoch = 100
batch_size = 64
display_step = 2  # 设置打印间隔

# =========《准备训练测试》==========
init = tf.global_variables_initializer()

total_batch = mnist.train.num_examples // batch_size  # 计算batch数量取整
print("共有%d个batch，每个batch大小为：%d" % (total_batch, batch_size))

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epoch):
        avg_loss = 0  # 储存所有batch平均loss值

        for i_batch in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            batch_xs = batch_xs.reshape(batch_size, num_steps, dim_input)
            feed_dict = {x_data: batch_xs, y_real: batch_ys}
            sess.run(op, feed_dict=feed_dict)  # 不断的进行优化
            avg_loss += sess.run(loss, feed_dict=feed_dict)

        avg_loss = avg_loss / total_batch

        # 打印
        if epoch % display_step == 0:
            print("Epoch:%3d/%3d, loss:%.6f" % (epoch, training_epoch, avg_loss))

            feed_dict = {x_data: batch_xs, y_real: batch_ys}
            train_accuracy = sess.run(accuracy, feed_dict=feed_dict)
            print("训练准确率:%.6f" % train_accuracy)

            test_imgs = test_imgs.reshape(num_test, num_steps, dim_input)
            feed_dict = {x_data: test_imgs, y_real: mnist.test.labels}
            test_accuracy = sess.run(accuracy, feed_dict=feed_dict)
            print("测试准确率:%.6f" % test_accuracy) 
