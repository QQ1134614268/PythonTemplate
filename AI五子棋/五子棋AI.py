# -*- coding: utf-8 -*-

import time
from tkinter import *
from tkinter import messagebox 

root = Tk()
root.title('五子棋')
SIZE = 17
win_flag = 0  # -1是人赢,1是电脑赢
w = Canvas(root, width=SIZE * 30, height=SIZE * 30, background='orange')  # canvas(结构化的图形，用于绘制图形，创建图形编辑器以及实现自定制的小构件类)
w.pack()
for num in range(1, SIZE):
    w.create_line(num * 30, 30, num * 30, (SIZE - 1) * 30, width=2)
for num in range(1, SIZE):
    w.create_line(30, num * 30, (SIZE - 1) * 30, num * 30, width=2)

color_flag = 1  # 下一步要下黑子
STEP = 0  # 为0则表示还没落第一个子
matrix = [[0 for i in range(SIZE + 2)] for i in range(SIZE + 2)]  # 外面pading了一圈  产生18*18的矩阵,值为0
print("matrix  ", matrix)
# matrix_copy = [[0 for i in range(SIZE+2)] for i in range(SIZE+2)] #外面pading了一圈
min_x = 0  # 当前棋子最左的范围  ????
min_y = 0  # 当前棋子最上的范围
max_x = 0
max_y = 0

# // "来表示整数除法，返回不大于结果的一个最大的整数，而" / " 则单纯的表示浮点数除


def fresh_outline_rectangle(x, y):  # 刷新棋子外接矩形范围
    global min_x
    global max_x
    global min_y
    global max_y
    global STEP
    if (STEP == 0):  # 下第一颗棋
        min_x = x
        min_y = y
        max_x = x
        max_y = y
    #        STEP = 1
    else:
        if (x < min_x):
            min_x = x
        elif (x > max_x):
            max_x = x
        if (y < min_y):
            min_y = y
        elif (y > max_y):
            max_y = y

# w.create_rectangle(30*min_x,30*min_y,30*max_x,30*max_y,fill='blue',outline='blue')


# 棋型的评估分数
shape_score = {(0, 1, 0): 5,  # 单子
               (0, 1, 1, -1): 10,  # 死2
               (-1, 1, 1, 0): 10,  # 死2
               (0, 1, 1, 0): 20,  # 活2
               (-1, 1, 1, 1, 0): 20,  # 死3
               (0, 1, 1, 1, -1): 20,  # 死3
               (0, 1, 1, 1, 0): 45,  # 活3
               (-1, 1, 1, 1, 1, 0): 60,  # 死4
               (0, 1, 1, 1, 1, -1): 60,  # 死4
               (0, 1, 1, 1, 1, 0): 120,  # 活4
               (0, 1, 1, 1, 1, 1, 0): 300,  # 成5
               (0, 1, 1, 1, 1, 1, -1): 300,
               (-1, 1, 1, 1, 1, 1, 0): 300,
               (-1, 1, 1, 1, 1, 1, -1): 300,
               (-1, 1, 1, 1, 1, 1, 1, -1): 300,
               (-1, 1, 1, 1, 1, 1, 1, 1, -1): 300,
               }


def evaluate_each(list_ad, list_xw, list_ze,
                  list_cq):  # 对一个节点的估值  list_ad, [0, 1, 0] list_xw  [0, 1, 0]  list_ze  [0, 1, 0]  list_cq  [0, 1, 0]
    score_right = shape_score.get(tuple(list_ad), 0)  # 默认为0  如果字典没有该 key,返回 value 0 ,, 向右
    score_down = shape_score.get(tuple(list_xw), 0)
    score_right_down = shape_score.get(tuple(list_ze), 0)
    score_right_up = shape_score.get(tuple(list_cq), 0)
    rank = [score_right, score_down, score_right_down, score_right_up]
    rank.sort()
    rank.reverse()
    score = rank[0] + rank[1]  # 当前节点的最大评分值
    return score


def get_list(mx, my, color):  # 从当前节点搜索 出来4个列表(四个方向),这里colorflag是局部变量
    print("从当前节点搜索")
    # ###################list_ad  ad---------- 右 方向
    global matrix
    list1 = []
    tx = mx
    ty = my
    while matrix[tx][ty] == color:
        list1.append(1)  # 1表示是己方棋子，-1是地方棋子
        tx = tx + 1  # 右
        ty = ty
    if matrix[tx][ty] == -color or tx == 0 or ty == 0 or tx >= SIZE or ty >= SIZE:
        list1.append(-1)
    else:
        list1.append(0)
    list1.pop(0)  # 删除自己 防止在合并的时候重复计算
    list2 = []
    tx = mx
    ty = my
    while (matrix[tx][ty] == color):
        list2.append(1)
        tx = tx - 1
        ty = ty
    if (matrix[tx][ty] == -color or tx == 0 or ty == 0 or tx >= SIZE or ty >= SIZE):
        list2.append(-1)
    else:
        list2.append(0)
    list2.reverse()
    list_ad = list2 + list1

    # ######################### list_xw  ------- 向下-
    list1 = []
    tx = mx
    ty = my
    while (matrix[tx][ty] == color):
        list1.append(1)
        tx = tx
        ty = ty + 1
    if (matrix[tx][ty] == -color or tx == 0 or ty == 0 or tx >= SIZE or ty >= SIZE):
        list1.append(-1)
    else:
        list1.append(0)
    list1.pop(0)
    list2 = []
    tx = mx
    ty = my
    while matrix[tx][ty] == color:
        list2.append(1)
        tx = tx
        ty = ty - 1
    if matrix[tx][ty] == -color or tx == 0 or ty == 0 or tx >= SIZE or ty >= SIZE:
        list2.append(-1)
    else:
        list2.append(0)
    list2.reverse()
    list_xw = list2 + list1

    ###########################list_ze   ---------右下
    list1 = []
    tx = mx
    ty = my
    while (matrix[tx][ty] == color):
        list1.append(1)
        tx = tx + 1
        ty = ty + 1
    if (matrix[tx][ty] == -color or tx == 0 or ty == 0 or tx >= SIZE or ty >= SIZE):
        list1.append(-1)
    else:
        list1.append(0)
    list1.pop(0)
    list2 = []
    tx = mx
    ty = my
    while (matrix[tx][ty] == color):
        list2.append(1)
        tx = tx - 1
        ty = ty - 1
    if (matrix[tx][ty] == -color or tx == 0 or ty == 0 or tx >= SIZE or ty >= SIZE):
        list2.append(-1)
    else:
        list2.append(0)
    list2.reverse()
    list_ze = list2 + list1

    #######################list_cq     --左下
    list1 = []
    tx = mx
    ty = my
    while (matrix[tx][ty] == color):
        list1.append(1)
        tx = tx + 1
        ty = ty - 1
    if (matrix[tx][ty] == -color or tx == 0 or ty == 0 or tx >= SIZE or ty >= SIZE):
        list1.append(-1)
    else:
        list1.append(0)
    list1.pop(0)
    list2 = []
    tx = mx
    ty = my
    while (matrix[tx][ty] == color):
        list2.append(1)
        tx = tx - 1
        ty = ty + 1
    if (matrix[tx][ty] == -color or tx == 0 or ty == 0 or tx >= SIZE or ty >= SIZE):
        list2.append(-1)
    else:
        list2.append(0)
    list2.reverse()
    list_cq = list2 + list1
    return [list_ad, list_xw, list_ze, list_cq]


def first_step():
    print("第一步")
    if matrix[SIZE // 2][SIZE // 2] == 0:
        down_chess(SIZE // 2, SIZE // 2)
    else:
        down_chess(SIZE // 2, SIZE // 2 + 1)


def is_out(min_x, min_y, max_x, max_y):  # 判断搜索范围有无出界
    print("判断搜索范围有无出界")
    if (min_x - 2 < 1):  # 判断有无出界
        temp_min_x = 1
    else:
        temp_min_x = min_x - 2
    if (min_y - 2 < 1):
        temp_min_y = 1
    else:
        temp_min_y = min_y - 2
    if (max_x + 2 >= SIZE):
        temp_max_x = SIZE
    else:
        temp_max_x = max_x + 2
    if (max_y + 2 >= SIZE):
        temp_max_y = SIZE
    else:
        temp_max_y = max_y + 2
    return [temp_min_x, temp_min_y, temp_max_x, temp_max_y]


def ai_go():  # ai搜索一下棋盘 然后走一步
    print(" ai搜索一下棋盘 然后走一步")
    global min_x
    global max_x
    global min_y
    global max_y
    global color_flag
    global matrix
    global matrix_copy
    time_start = time.time()
    evaluate_matrix = [[0 for i in range(SIZE + 2)] for i in range(SIZE + 2)]  # 记录每个节点估值
    if (STEP == 1):
        first_step()
    else:  # 确定搜索边界
        #        for i in range(SIZE+2):
        #            matrix_copy[i]=matrix[i].copy()#备份
        temp_min_x1, temp_min_y1, temp_max_x1, temp_max_y1 = is_out(min_x, min_y, max_x, max_y)  # 第一层搜索范围
        evaluate_matrix = [[0 for i in range(SIZE + 2)] for i in range(SIZE + 2)]  # 记录每个节点估值  第一层-------------------
        evaluate_matrix2 = [[0 for i in range(SIZE + 2)] for i in range(SIZE + 2)]  # 第二层的估值矩阵
        Max = -100000
        for i in range(temp_min_x1, temp_max_x1 + 1):
            for j in range(temp_min_y1, temp_max_y1 + 1):
                cut_flag = 0  # 是否剪枝的标记
                evaluate_matrix2 = [[0 for i in range(SIZE + 2)] for i in range(SIZE + 2)]  # 第二层的估值矩阵
                if (matrix[i][j] == 0):
                    matrix[i][j] = color_flag  # AI走一步
                    temp_min_x2, temp_min_y2, temp_max_x2, temp_max_y2 = is_out(temp_min_x1, temp_min_y1, temp_max_x1,
                                                                                temp_max_y1)  # 第二层搜索范围
                    for ii in range(temp_min_x2, temp_max_x2 + 1):  # 获得第二层的估值矩阵
                        for jj in range(temp_min_y2, temp_max_y2 + 1):
                            if (matrix[ii][jj] == 0):
                                # 计算估值(MIN节点)
                                matrix[ii][jj] = -color_flag
                                [list_ad, list_xw, list_ze, list_cq] = get_list(ii, jj, -color_flag)  # 对人走的进行估值
                                evaluate_matrix2[ii][jj] = -evaluate_each(list_ad, list_xw, list_ze,
                                                                          list_cq) * 2 + 0.1  # 获得所有节点的估价值
                                [list_ad, list_xw, list_ze, list_cq] = get_list(i, j, color_flag)
                                evaluate_matrix2[ii][jj] = evaluate_matrix2[ii][jj] + evaluate_each(list_ad, list_xw,
                                                                                                    list_ze,
                                                                                                    list_cq)  # 对AI估值
                                matrix[ii][jj] = 0
                                # 剪枝
                                if (evaluate_matrix2[ii][jj] < Max):
                                    # print("剪枝！当前位置：",i,j,"剪枝！当前估价值：",evaluate_matrix2[ii][jj],"Max估价值：",Max,"ii=",ii,"jj=",jj)
                                    evaluate_matrix[i][j] = evaluate_matrix2[ii][jj]
                                    cut_flag = 1

                                # elif(evaluate_matrix2[ii][jj]>Max):break
                                # print("不剪枝！当前位置：",i,j,"估价值",evaluate_matrix2[ii][jj],"Max估价值：",Max)

                        if (cut_flag == 1):
                            break
                    # 找最小值

                    if (cut_flag == 0):
                        Min = 1000000
                        for ii in range(temp_min_x2, temp_max_x2 + 1):  # 找最小估值
                            for jj in range(temp_min_y2, temp_max_y2 + 1):
                                if (evaluate_matrix2[ii][jj] < Min and matrix[ii][jj] == 0 and evaluate_matrix2[ii][
                                    jj] != 0):
                                    Min = evaluate_matrix2[ii][jj]
                        evaluate_matrix[i][j] = Min
                        # 更新Max
                        if (Max < Min):
                            Max = Min
                            candidate_x = i
                            candidate_y = j
                    matrix[i][j] = 0

        '''
        #找最大值                        
        Max2=-100000
        candidate_x=0
        candidate_y=0
        for i in range(temp_min_x1,temp_max_x1+1):#找最大估值作为候选人
            for j in range(temp_min_y1,temp_max_y1+1):
                if(evaluate_matrix[i][j]>Max2 and matrix[i][j]==0 and evaluate_matrix[i][j]!=0 ):
                    Max2=evaluate_matrix[i][j]
                    candidate_x=i
                    candidate_y=j


        print("Max:",Max2)
        print("Minx:",temp_min_x1,"Miny:",temp_min_y1)
        for a in range(SIZE+2):
            print(evaluate_matrix[a])

        print("MATRIX:")
        for a in range(SIZE+2):
            print(matrix[a])
        print(candidate_x,candidate_y)
        print("matrix(x,y):",matrix[candidate_x][candidate_y])
        #matrix[candidate_x][candidate_y] = color_flag
        '''
        down_chess(candidate_x, candidate_y)
        time_end = time.time()
        print('Time cost:', round(time_end - time_start, 4), 'second')


def action(event):  # 响应点击
    print("响应点击")
    mx = event.x
    my = event.y
    if mx % 30 < 15:
        xin_x = mx // 30 * 30
    else:
        xin_x = mx // 30 * 30 + 30
    if my % 30 < 15:
        xin_y = my // 30 * 30
    else:
        xin_y = my // 30 * 30 + 30
    int_x = xin_x // 30
    int_y = xin_y // 30
    if matrix[int_x][int_y] == 0 and win_flag == 0:
        down_chess(int_x, int_y)
        if win_flag == 0:
            ai_go()


def down_chess(int_x, int_y):  # 画一个棋子并记录
    print("画一个棋子并记录")
    # event.x 鼠标左键的横坐标
    # event.y 鼠标左键的纵坐标
    global matrix
    global color_flag
    global STEP
    global win_flag
    if int_x != 0 and int_y != 0 and int_x < SIZE and int_y < SIZE and matrix[int_x][int_y] == 0:
        matrix[int_x][int_y] = color_flag
        fresh_outline_rectangle(int_x, int_y)
        x1, y1 = (int_x * 30 - 15), (int_y * 30 - 15)
        x2, y2 = (int_x * 30 + 15), (int_y * 30 + 15)
        STEP = STEP + 1
        #        print("Step:",STEP)
        if color_flag == 1:
            w.create_oval(x1, y1, x2, y2, fill='black')
            label = Label(root, text=str(STEP), bg='black', fg="white")  # 标数字
            label.place(x=x1 + 5, y=y1 + 3)
        else:
            w.create_oval(x1, y1, x2, y2, fill='white', width=2)
            label = Label(root, text=str(STEP), bg='white', fg="black")
            label.place(x=x1 + 5, y=y1 + 3)
        [list_ad, list_xw, list_ze, list_cq] = get_list(int_x, int_y, color_flag)
        if sum(list_ad[1:-1]) >= 5 or sum(list_xw[1:-1]) >= 5 or sum(list_ze[1:-1]) >= 5 or sum(list_cq[1:-1]) >= 5:
            if color_flag == 1:
                messagebox.showinfo(title='Game Over', message='Black_Win (^-^)')
                win_flag = 1
            else:
                messagebox.showinfo(title='Game Over', message='White_Win (^-^)')
                win_flag = -1
        color_flag = -color_flag

    else:
        pass


first_step()
# 画布与鼠标左键进行绑定
w.bind("<Button-1>", action)
mainloop()
