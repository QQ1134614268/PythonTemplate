# coding:UTF-8
import matplotlib.pyplot as plt
import numpy as np

# #画直线
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()

# ###画散点图(研究相关性）scatter
# # c 颜色，s点大小，alpha透明度,marker 点形状

height = [161, 170, 182, 175, 173, 165]
weight = [50, 58, 80, 70, 69, 55]
plt.scatter(height, weight)
plt.show()

m = 1000
x = np.random.randn(m)
y = -x + np.random.randn(m) * 0.5
plt.scatter(x, y, c='r', s=200, alpha=0.5)
plt.show()

# #画折线图
x = np.linspace(-10, 10, 5)
y = x ** 2
plt.plot(x, y)
plt.show()

# ##画条形图
N = 5
y = [20, 10, 30, 25, 15]
index = np.arange(N)
plt.bar(left=index, height=y, color='red', width=0.5)
plt.show()

####饼状图
labels1 = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]
explode1 = [0, 0.05, 0.08, 0]
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels1, autopct='%.0f%%', explode=explode1, shadow=True)
plt.show()

####箱型图
np.random.seed(1000)
data = np.random.normal(size=(1000, 5), loc=0, scale=1)
labes = ["A", "B", "C", "D", "E"]
plt.boxplot(data, sym='o', whis=1.5, labels=labes)
plt.show()

# #直方图
mu = 100
sigma = 20
x = mu + sigma * np.random.randn(20000)
plt.hist(x, bins=100, color='green', normed=False)
plt.show()
