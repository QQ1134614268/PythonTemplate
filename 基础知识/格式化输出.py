'''
Created on 2018年6月8日

@author: Administrator
'''
import builtins
print(dir(builtins))


# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
if True:
    msg = 'I am from Runoob'

print(msg)

# 输出格式美化
# Python两种输出值的方式: 表达式语句和 print() 函数。
# 
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
# 
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。

s = 'Hello, Runoob'
str(s)
repr(s)
str(1/7)
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# write()
import sys
sys.stdout.write("stdout")
 
 

print('%o' % 20) # 八进制24
print('%d' % 20) # 十进制20
print('%x' % 24) # 十六进制18 

print('%f' % 1.11)         # 默认保留6位小数1.110000
print('%.1f' % 1.11)       # 取1位小数1.1
print('%e' % 1.11)         # 默认6位小数，用科学计数法1.110000e+00
print('%.3e' % 1.11)       # 取3位小数，用科学计数法1.110e+00
print('%g' % 1111.1111)    # 默认6位有效数字1111.11
print('%.7g' % 1111.1111)  # 取7位有效数字1111.111
print('%.2g' % 1111.1111)  # 取2位有效数字，自动转换为科学计数法1.1e+03 

print('%s' % 'hello world')       # 字符串输出hello world
print('%20s' % 'hello world')     # 右对齐，取20位，不够则补位         hello world
print('%-20s' % 'hello world')    # 左对齐，取20位，不够则补位hello world         
print('%.2s' % 'hello world')     # 取2位he
print('%10.2s' % 'hello world')   # 右对齐，取2位        he
print('%-10.2s' % 'hello world')  # 左对齐，取2位he        