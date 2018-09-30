# 
# # 使用命令行执行  python  文件名.py   参数一  参数二   ，否则报错
# import sys
# 
# print('命令行参数如下:')
# for i in sys.argv:
#    print(i)
# 
# #====================
# print('\n\nPython 路径为：', sys.path, '\n')
# 
# class people:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# 
#     def __str__(self):
#         return '这个人的名字是%s,已经有%d岁了！'%(self.name,self.age)
# 
# a=people('孙悟空',999)
#  
# print(a)
# 
# 
# 
# 
# import urllib
# from urllib.request import urlopen
# from urllib.parse import urlencode
# 
# url='http://www.xxx.com/login'
# MNIST_data={"username":"admin","password":123456}
# req_data=urlencode(MNIST_data)#将字典类型的请求数据转变为url编码
# res=urlopen(url+'?'+req_data)#通过urlopen方法访问拼接好的url
# res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
# 
# print(res)
# #处理post请求,如果传了data，则为post请求
# 
# import urllib
# from urllib.request import Request
# from urllib.parse import urlencode
# 
# url='http://www.baidu.com'
# MNIST_data={"username":"admin","password":123456}
# MNIST_data=urlencode(MNIST_data)#将字典类型的请求数据转变为url编码
# MNIST_data=MNIST_data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
# req_data=Request(url,MNIST_data)#将url和请求数据处理为一个Request对象，供urlopen调用
# with urlopen(req_data) as res:
#     res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
# 
# print(res)

''' http://www.runoob.com/python/python-reg-expressions.html  参考网址'''
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配


# 可写函数说明
def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4]);   
    print ("函数内取值: ", mylist)
    return
 
# 调用changeme函数  mylist   list ???
mylist = [10,20,30];
changeme( mylist );
print ("函数外取值: ", mylist)

