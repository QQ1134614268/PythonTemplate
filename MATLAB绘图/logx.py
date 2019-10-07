import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimHei'  # 用来正常显示中文标签
# plt.rcParams['font.sas-serig']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# x轴的范围    linspace(x轴起点,x轴终点,采集样点数)
x = np.linspace(0.00000001, 10, 10000)
y = x * np.log2(x)
# 画布大小  创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px  
plt.figure(figsize=(7, 7))
# 在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）  
plt.plot(x, y, label="$y=f(x)$", color="red", linewidth=0.5)
# X轴的文字  
plt.xlabel("X")
# Y轴的文字  
plt.ylabel("Y")
# 图表的标题  
plt.title("标题: xlogx")
# #Y轴的范围  
# plt.ylim(-10,10)  
# 保存图  
plt.savefig("xlogx.jpg")
# 显示图示  
plt.legend()
# 显示图  
plt.show()
