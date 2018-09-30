import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, BatchNormalization
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LearningRateScheduler

train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")
Y_train = train_data["label"] #defining labels as Y_train
X_train = train_data.drop(labels = ["label"],axis = 1) #defining the images as X_train
g = plt.imshow(X_train[100][:,:,0]) #displaying random image from the dataset

X_train = X_train / 255.0
X_train = X_train.astype('float32')
X_test = test_data / 255.0
X_test = X_test.astype('float32')
X_train = X_train.values.reshape(X_train.shape[0],28,28,1)
X_test = X_test.values.reshape(X_train.shape[0],28,28,1)
Y_train = to_categorical(Y_train, num_classes = 10)

datagen = ImageDataGenerator(
rotation_range=10,
zoom_range = 0.1,
width_shift_range=0.1,
height_shift_range=0.1)
datagen  . fit(X_train)
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size = 0.1)
# 带有5个卷积层的CNN 该CNN的输入张量shape（image_height，image_width，image_channels）。在这种情况下，我将CNN配置为处理大小为（28,28,
# 1）的输入。我通过将参数input_shape =（28,28,1）传递给第一层来完成此操作。
# Conv2D层用于卷积运算，它通过在输入图像上滑动卷积滤波器来生成特征图，从而从输入图像中提取特征。这里我选择模型第一组的feature map大小为5 x 5，第二组和第三组的feature map大小为3 x 3。
# MaxPooling2D层用于max-pooling操作，减少了每个特性的维数，这有助于缩短训练时间和减少参数数量。这里我为所有组选择大小为2 x 2的pooling window。
# 为了归一化输入层，我使用BatchNormalization层来调整和缩放激活。Batch Normalization通过隐藏单元值的移位(协方差移位)来减少数量。此外，它还允许网络的每一层独立于其他层学习。
# 为了对抗过拟合，我使用了drop - outs层，这是一种强大的正则化技术。drop - out是用来减少过拟合的方法。它通过在学习阶段随机禁用神经元，迫使模型学习同一数据的多个独立表示。例如，层将随机禁用所有组中40%的输出。
# 最后，我们使用Flatten（）将图像维度降低到1D，并在顶部添加2个Dense全连接层。Dense 层为我们的输出处理1D图像矢量。
# 我做10个分类，因为数据集中有10个输出标签。Softmax激活使我能够根据概率计算输出。为每个类分配概率，具有最大概率的类是输入的模型输出。 所有其他层，我使用“ relu”激活函数，因为“ relu”通过加快训练过程来改善神
# 经网络。
model = Sequential()
model.add(Conv2D(32, kernel_size=5,input_shape=(28, 28, 1), activation = 'relu'))
model.add(Conv2D(32, kernel_size=5, activation = 'relu'))
model.add(MaxPool2D(2,2))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Conv2D(64, kernel_size=3,activation = 'relu'))
model.add(Conv2D(64, kernel_size=3,activation = 'relu'))
model.add(MaxPool2D(2,2))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Conv2D(128, kernel_size=3, activation = 'relu'))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dense(256, activation = "relu"))
model.add(Dropout(0.4))
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.4))
model.add(Dense(10, activation = "softmax"))
# 让我们现在编译我们的模型并在其上添加一个优化器。我使用了categorical_crossentropy作为损失函数，Adam使用了该模型的优化器。
# 优化器负责通过反向传播更新神经元的权重。它计算损失函数相对于每个权重的导数，并从权重中减去它。这就是神经网络学习的方式。
optimizer=Adam(lr=0.001)
model.compile(optimizer = optimizer , loss = "categorical_crossentropy", metrics=["accuracy"])
model.summary()

model_try = model.fit_generator(datagen.flow(X_train,Y_train, batch_size=32),
epochs = 30, validation_data = (X_val,Y_val),
verbose = 1, steps_per_epoch=300)
predictions = model.predict(X_test)
predictions = np.argmax(predictions,axis = 1)
predictions = pd.Series(predictions, name="Label")
submit = pd.concat([pd.Series(range(1,28001),name = "ImageId"),predictions],axis = 1)
submit.to_csv("result.csv",index=False)
# 我能够获得高达99.571％的测试精度！