from math import pi

a = b = c = 1
a, b, c = 1, 2, "john"
print(a, b, c)
c = complex(1, 2)
print(c)
 
tuples = ('runoob', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')

for ss in "'Python'":  # 第一个实例
    print('当前字母 :', ss)
   
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])
 
print("Good bye!")

a = -1
print(abs(a * pi))

var1 = 'Hello World!'

print ("更新字符串 :- ", var1[:6] + 'Runoob!')

var1 = 'Hello World!'
var2 = "Python Runoob"

print("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
 
a = {'Name': 'Tom', 'Age': 7, 'Class': 'First'};

"""字典"""
print ("dict['Name']: ", a['Name'])
print ("dict['Age']: ", a['Age'])

a['Age'] = 8;  # update existing entry
print ("dict['Age']: ", a['Age'])

# del dict['Name']; # 删除键是'Name'的条目
# dict.clear();     # 清空词典所有条目
# del dict ;        # 删除词典

maps = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};
 
print ("dict['Name']: ", maps['Name']);

