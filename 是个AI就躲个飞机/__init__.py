import os
print(os.name)
path = 'C:\Windows\Fonts'.replace("\\", '/') + '/'

print(path)


t=True if 0 >= 1 else False
print(t)

#****************定义************************定义从何而来,,起源--如果被过半接受,接受,,类区块链
tl = lambda x :x<3 and 0 or 99 #and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
# or	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
print(tl(1))

# is	is 是判断两个标识符是不是引用自一个对象
#
# is not	is not 是判断两个标识符是不是引用自不同对象
# in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
# not in	如果在指定的序列中没有找到值返回 True，否则返回 False。
# and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
# or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。