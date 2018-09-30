
rank=[0,1,3,2]
rank.sort()
print(rank)
import matplotlib
for i in range( 2):
    print(i)
max_y = 0
# // "来表示整数除法，返回不大于结果的一个最大的整数，而" / " 则单纯的表示浮点数除
print(max_y)
def fresh_outline_rectangle( ):  # 刷新棋子外接矩形范围
    global max_y
    max_y=9
    print(max_y)
fresh_outline_rectangle()
print(max_y)


# from tkinter import *
# from tkinter import messagebox
# import time
#
# root = Tk()
# root.title('五子棋')
# SIZE = 17
# win_flag = 0  # -1是人赢,1是电脑赢
# w = Canvas(root, width=SIZE * 30, height=SIZE * 30, background='orange')#canvas(结构化的图形，用于绘制图形，创建图形编辑器以及实现自定制的小构件类)
# w.pack()
# for num in range(1, SIZE):
#     w.create_line(num * 30, 30, num * 30, (SIZE - 1) * 30, width=2)# num * 30   30
# for num in range(1, SIZE):
#     w.create_line(30, num * 30, (SIZE - 1) * 30, num * 30, width=2)
#
# # first_step()
# # # 画布与鼠标左键进行绑定
# # w.bind("<Button-1>", action)
# mainloop()