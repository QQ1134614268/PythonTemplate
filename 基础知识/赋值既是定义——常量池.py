'''
Created on 2018年3月26日

@author: Administrator
'''
# 重要::变量没有声明定义，赋值既是重新定义；原来变量空间被回收；可变函数传递与新建内部函数，新建优先，赋值即为新建函数，赋值既是重新定义

def changeme( mylist ):
    print(  id(mylist ))
    "修改传入的列表"
    mylist = [1,2,3,4];
    print(  id(mylist ))
    print ("函数内取值: ", mylist)
    return
 
# 调用changeme函数
mylist = [10,20,30];
print(  id(mylist ))
mylist = [10,20,30];
print(  id(mylist ))
mylist = [10,20,31];
print(  id(mylist ))
changeme( mylist );
print ("函数外取值: ", mylist)
#内建变量？？，如果定义变量存在，则地址不变，难道是常量池作用，寻找常量，是否存在，若存在返回地址；应该是这样
x = int(3.3)
print(  id(x ))
x = 0
print(  id(x ))
x = 1
print(  id(x ))
x = 2
print(  id(x ))
x = 6
print(  id(x ))
x = 4
print(  id(x ))
x = 5
print(  id(x ))
x = 6
print(  id(x ))
y = 6
print(  id(y ))




#赋值即是定义，如此函数内有两个a变量名。冲突,报错--
#在java静态语言中，--int a=0; void add(){int a=1;}--变量名冲突报错,函数内可以访问函数外变量，内部定义a，冲突。或者取a，两者取谁的？？冲突
a = 10
print(id(a))
def mysum ( n ) :
    n += a
    print(id(a))
    a = 11
    print(id(a))
    print ('a = ', a, end = ' , ' )
    print ( 'n = ', n )
  
mysum(3)


##生成常量后在常量池中寻找，若存在，返回地址，同时保持常量池中常量唯一性
a=1
print(id(a))
b=6
print(id(1))
print(id(b))
print (id(2*3))

