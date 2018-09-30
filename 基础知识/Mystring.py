'''
Created on 2018年2月9日

@author: Administrator
'''
from math import *

a = b = c = 1
a, b, c = 1, 2, "john"
print(a,b,c)
c=complex(1,2)
print(c)

print(str)
 
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')



for ss in "'Python'":     # 第一个实例
    print( '当前字母 :', ss)
   
   
   
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print( '当前水果 :', fruits[index])
 
print( "Good bye!")

a=-1
print(abs(a*pi))


var1 = 'Hello World!'

print ("更新字符串 :- ", var1[:6] + 'Runoob!')

var1 = 'Hello World!'
var2 = "Python Runoob"

print( "var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])