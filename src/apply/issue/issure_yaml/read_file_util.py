#  todo todo
#   children 结构是同一个类

#   yaml tree json arr 工具类
#  tree
#  yaml, prop(path) 一维, (path路径, 一维唯一属性)
#  dict(class),json,, 图 二维的

# 文件(yaml, prop, json)->dict->class

# yaml 文件转 json
# 文件
#     yaml
#     prop
#     json

# class, dict -> tree(children)

import json
from unittest import TestCase


class Catalog:
    name: str
    children: list


def prop_to_dict(lines):
    # lines = ["dev/lib/xx=2", "dev/bin/xx=3"]
    pass


def prop_to_dict(lines):
    # lines = ["dev/lib/xx", "dev/bin/xx"]
    root = {}
    for index, line in enumerate(lines):
        arr = line.split("/")
        change(arr, root)
    return root


def prop_to_dict_v2(lines):
    # lines = ["dev/lib/xx", "dev/bin/xx"]
    root = []
    for index, line in enumerate(lines):
        arr = line.split("/")
        change2(arr, root)
    return root


def change2(paths, root):
    c_list = root
    for path in paths:
        if path not in [c.get("name") for c in c_list]:
            c_list.append({"name": path, "children": []})
        for c in c_list:
            if c.get("name") == path:
                c_list = c.get("children")


# 模拟文件夹, 根据路径,从根目录开始, 切换当前目录. 不存在时就创建
def change(paths, dic):
    c_path = dic
    for path in paths:
        if path not in c_path:
            c_path[path] = {}
        c_path = c_path[path]


def get_parent_path(path_arr, dic):
    p_path = {}
    for path in path_arr:
        p_path = dic[path]
    return p_path


def y2j():
    pass


class Y2J:
    file = "xx.yaml"

    #
    def to_json(self):
        pass


class Path2Json:
    pass


class Class2Json:

    def to_json(self):
        pass

    def to_json(self):
        pass

    def example(self):
        pass

    pass


class Child2Json:

    def to_json(self):
        pass

    def to_json(self):
        pass


class TestAutoCode(TestCase):
    def test_to_prop(self):
        root = []
        for index, val in enumerate(["广东", "广西"]):
            p = Area(val, order=index)
            for city_index, city in enumerate(["1", "2"]):
                c = Area(val + city + "市", order=city_index)
                p.children.append(c)
            root.append(p)
        with open("area.json", "w+", encoding="utf-8") as f:
            f.write(json.dumps(root, cls=MyJsonEncoder, ensure_ascii=False, indent=2))

    def test_2(self):
        lines = ["dev/lib/xx", "dev/bin/xx"]
        prop_to_dict(lines)

    def test_prop_to_dict_v2(self):
        lines = ["dev/lib/xx", "dev/bin/xx"]
        prop_to_dict_v2(lines)


class Area:
    def __init__(self, name, order=1):
        self.name = name
        self.order = order
        self.children = []


class MyJsonEncoder(json.JSONEncoder):
    # def default(self, o):
    #     try:
    #         iterable = iter(o)
    #     except TypeError:
    #         pass
    #     else:
    #         return list(iterable)
    #     # Let the base class default method raise the TypeError
    #     return JSONEncoder.default(self, o)

    def default(self, o):
        try:
            return super().default(self, o)
        except:
            return o.__dict__
            # return super().default(self, o)
