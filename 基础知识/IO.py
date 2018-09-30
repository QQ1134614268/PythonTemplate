# 打开一个文件
fo = open("foo.txt", "wb")
print ("文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)
print ("访问模式 : ", fo.mode)
# print( "末尾是否强制加空格 : ", fo.softspace )

# 关闭打开的文件
fo.close()


# 打开一个文件
fo = open("foo.txt", "w")
fo.write( "www.runoob.com!\nVery good site!\n")
 
# 关闭打开的文件
fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
strs = fo.read(10)
print ("读取的字符串是 : ", strs)
print ("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("读取的字符串是 : ", str)
 
# 查找当前位置
position = fo.tell()
print ("当前文件位置 : ", position)
 
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print ("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()


import os

# 重命名文件test1.txt到test2.txt。
open("test1.txt",'w')
os.rename( "test1.txt", "test2.txt" )
# 删除一个已经存在的文件test2.txt
os.remove("test2.txt")
# 创建目录test
# os.mkdir("test")
# 
# 将当前目录改为"/test"
# os.chdir("/test")
# 
# # 给出当前的目录
print (os.getcwd())
# 
# # 删除”/tmp/test”目录
# os.rmdir( "/test"  )
 