import os


def getOrMakeDir(path):  # return  0:已经存在;1:创建成功;-1 未知结果
    # 去除首位空格   # 去除尾部 \ 符号
    path = path.strip().rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return 1
    else:
        return 0
    return -1


def getOrMakeFile(path):  # return  0:已经存在;1:创建成功;-1 未知结果
    # 去除首位空格   # 去除尾部 \ 符号
    path = path.strip().rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return 1
    else:
        return 0
    return -1

 
# 定义要创建的目录
path = "d:\\test\\web\\"
getOrMakeDir(path)
