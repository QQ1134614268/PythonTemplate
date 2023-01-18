from collections import namedtuple

# 基本例子
Point = namedtuple('Point', ['x', 'y'])  # 类名为Point,属性有'x'和'y'

p = Point(11, y=22)  # 用位置或关键字参数实例化，因为'x'在'y'前，所以x=11,和函数参数赋值一样的
print(p[0] + p[1])  # 我们也可以使用下标来访问
# 33

x, y = p  # 也可以像一个元组那样解析
print(x, y)
# (11, 22)

print(p.x + p.y)  # 也可以通过属性名来访问
# 33

print(p)  # 通过内置的__repr__函数，显示该对象的信息
# Point(x=11, y=22)
