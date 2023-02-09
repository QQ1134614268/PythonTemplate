# -*- coding:utf-8 -*-
"""
@Time: 2021/7/10
@Description:
"""


class Parent:
    aa = 1

    def __init__(self):
        self.par = 1

    def aa_func_parent(self):
        pass


class Child(Parent):
    bb = 1

    def __init__(self):
        super().__init__()
        self.chi = 1

    def aa_func_child(self):
        pass


# dir 列表,继承, 所有方法属性
# __dir__() 列表,继承,, obj所有方法属性
# __dict__ 字典,无继承, class类属性,obj实例属性,
print(dir(Parent), dir(Child), dir(Parent()), dir(Child()), sep='\n')
print(Parent().__dir__(), Child().__dir__(), sep='\n')
print(Parent.__dict__, Child.__dict__, Parent().__dict__, Child().__dict__, sep='\n')
