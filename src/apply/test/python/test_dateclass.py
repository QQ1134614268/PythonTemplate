from dataclasses import dataclass, field
from typing import Any


# 类变量, dataclass, namedtuple, 实例变量

# dataclass:
#   默认添加 所有field作为参数的__init__ ;
#   字段可以被提示
#   默认__init__ 实例化需要实例化全部,
#   自定义无参 init 需要在field中实例化
@dataclass(order=True)
class User:
    _id: int
    item: Any = field(compare=False)


@dataclass
class Person:
    _id: int = 1
    name: str = "tom"  # 可以被提示
    age: int = 22

    @property
    def password(self):
        return self.name

    @staticmethod
    def get_instance():
        return Person()


if __name__ == '__main__':
    print(Person.get_instance())
    print(Person(_id=3, name="123", age=12))
