# coding=utf-8

""""VGG-style卷积神经网络实现mnist"""
# 读取数据

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
train_img = mnist.train.images
train_lab = mnist.train.labels
test_img = mnist.test.images
test_lab = mnist.test.labels

# 定义网络维度参数
dim_input = 784
dim_output = 10

# 定义数据集输入以及ground truth
x_data = tf.placeholder(tf.float32, [None, dim_input])  # 样本个数不确定，所以为None
y_real = tf.placeholder(tf.float32, [None, dim_output])

stddev = 0.1
weights = {"w_conv1": tf.Variable(tf.random_normal([3, 3, 1, 64], stddev=stddev)),
           "w_conv2": tf.Variable(tf.random_normal([3, 3, 64, 128], stddev=stddev)),
           "w_fc1": tf.Variable(tf.random_normal([7 * 7 * 128, 1024], stddev=stddev)),
           "w_fc2": tf.Variable(tf.random_normal([1024, dim_output], stddev=stddev))}

biases = {"b_conv1": tf.Variable(tf.zeros([64])),
          "b_conv2": tf.Variable(tf.zeros([128])),
          "b_fc1": tf.Variable(tf.zeros([1024])),
          "b_fc2": tf.Variable(tf.zeros([dim_output]))}


def forward_prop(_input, _w, _b, keep_prob):
    """
    搭建网络模型
    :param _input:
    :param _w:
    :param _b:
    :param keep_prob:
    """
    # 输入reshape
    _input_r = tf.reshape(_input, shape=[-1, 28, 28, 1])
    # 第一层卷积层
    _conv1 = tf.nn.conv2d(_input_r, _w["w_conv1"], strides=[1, 1, 1, 1], padding="SAME")
    _conv1 = tf.nn.relu(tf.nn.bias_add(_conv1, _b["b_conv1"]))
    # 池化层
    _pool1 = tf.nn.max_pool(_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
    # dropout
    _pool_dr1 = tf.nn.dropout(_pool1, keep_prob=keep_prob)

    # 第二层卷积层
    _conv2 = tf.nn.conv2d(_pool_dr1, _w["w_conv2"], strides=[1, 1, 1, 1], padding="SAME")
    _conv2 = tf.nn.relu(tf.nn.bias_add(_conv2, _b["b_conv2"]))
    _pool2 = tf.nn.max_pool(_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
    _pool_dr2 = tf.nn.dropout(_pool2, keep_prob=keep_prob)

    # flatten
    flatten = tf.reshape(_pool_dr2, shape=[-1, _w["w_fc1"].get_shape().as_list()[0]])

    # 第一层全连接层
    _fc1 = tf.nn.relu(tf.add(tf.matmul(flatten, _w["w_fc1"]), _b["b_fc1"]))
    # dropout
    _fc_dr1 = tf.nn.dropout(_fc1, keep_prob=keep_prob)

    # 第二层全连接层
    _out = tf.nn.relu(tf.add(tf.matmul(_fc_dr1, _w["w_fc2"]), _b["b_fc2"]))

    return {"input_r": _input_r, "conv1": _conv1, "pool1": _pool1, "pool_dr1": _pool_dr1, "conv2": _conv2,
            "pool2": _pool2, "pool_dr2": _pool_dr2, "flatten": flatten, "fc1": _fc1, "fc_dr1": _fc_dr1, "out": _out}


keep_prob = tf.placeholder(tf.float32)  # droupout

y_pred = forward_prop(x_data, weights, biases, keep_prob)["out"]
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_pred, labels=y_real))
op = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

# 定义准确率
correct = tf.equal(tf.arg_max(y_pred, 1), tf.arg_max(y_real, 1))  # 计算出预测值与真实值是否相等(独热码为1的索引是否相等)
accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))  # 每个batch的平均准确率 将True转成float

# 训练参数
training_epoch = 100
batch_size = 128
display_step = 2  # 设置打印间隔

# =========《准备训练测试》==========
init = tf.global_variables_initializer()

total_batch = mnist.train.num_examples // batch_size  # 计算batch数量取整
print("共有%d个batch，每个batch大小为：%d" % (total_batch, batch_size))

saver = tf.train.Saver(max_to_keep=2)
is_training = False

with tf.Session() as sess:
    sess.run(init)

    if is_training:
        for epoch in range(training_epoch):
            avg_loss = 0  # 储存所有batch平均loss值

            for i_batch in range(total_batch):
                batch_xs, batch_ys = mnist.train.next_batch(batch_size)
                feed_dict = {x_data: batch_xs, y_real: batch_ys, keep_prob: 0.5}
                sess.run(op, feed_dict=feed_dict)  # 不断的进行优化
                avg_loss += sess.run(loss, feed_dict=feed_dict)

            avg_loss = avg_loss / total_batch

            # 打印
            if epoch % display_step == 0:
                print("Epoch:%3d/%3d, loss:%.6f" % (epoch, training_epoch, avg_loss))

                feed_dict = {x_data: batch_xs, y_real: batch_ys, keep_prob: 0.5}
                train_accuracy = sess.run(accuracy, feed_dict=feed_dict)
                print("训练准确率:%.6f" % train_accuracy)

                # feed_dict = {x_data: mnist.test.images, y_real: mnist.test.labels, keep_prob: 1.0}
                # test_accuracy = sess.run(accuracy, feed_dict=feed_dict)
                # print("测试准确率:%.6f" % test_accuracy)

                saver.save(sess, "MNIST_model/model.ckpt-" + str(epoch))
    else:
        saver.restore(sess, tf.train.latest_checkpoint(checkpoint_dir="MNIST_model/"))
        feed_dict = {x_data: mnist.test.images, y_real: mnist.test.labels, keep_prob: 1.0}
        test_accuracy = sess.run(accuracy, feed_dict=feed_dict)
        print("测试准确率:%.6f" % test_accuracy)

    print("结束！") 
