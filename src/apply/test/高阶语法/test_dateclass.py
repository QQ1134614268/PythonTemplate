from dataclasses import dataclass


# 类变量, dataclass, namedtuple, 实例变量

# dataclass:
#   默认添加 所有field作为参数的__init__ ;
#   字段可以被提示
#   默认__init__ 实例化需要实例化全部,
#   自定义无参 init 需要在field中实例化


@dataclass()
class Person:
    def __init__(self):
        self.dd = 2  # 可以被提示

    aaa: str = 123  # 可以被提示
    name: str = "tom"
    age: int = 22

    @property
    def password(self):
        return self.name

    @staticmethod
    def get_instance():
        return Person()


if __name__ == '__main__':
    aa = Person.get_instance()
    print(aa)
    print(aa.name)
