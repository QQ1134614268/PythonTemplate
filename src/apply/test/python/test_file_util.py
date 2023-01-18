# -*- coding:utf-8 -*-
"""
@Time: 2022/8/9
@Description:
"""
from datetime import date
from unittest import TestCase

from util import class_dict_util
from util.cache_util import to_json_file
from util.file_util import get_data_dir,  FileUtil


class XmindVO:
    value: str
    space: int
    children: list


class User:
    def __init__(self, name=None, birth_day=None, address_list=[]):
        self.name = name
        self.birth_day = birth_day
        self.address_list = address_list


class Address:
    def __init__(self, province=None, city=None, county=None, info=None, ):
        self.province = province
        self.city = city
        self.county = county
        self.info = info


class Area:
    def __init__(self, area_name=None):
        self.area_name = area_name
        self.children = []


class TestFileConvert(TestCase):

    @to_json_file("area.json")
    def test_init_area_data(self):
        ret_list = []
        for i in range(3):
            level_1 = Area(area_name="sheng_" + str(i))
            ret_list.append(level_1)
            for j in range(3):
                level_2 = Area(area_name="city_" + str(j))
                level_1.children.append(level_2)
                for k in range(3):
                    level_3 = Area(area_name="区_" + str(k))
                    level_2.children.append(level_3)
        return ret_list

    def test_init_address_data(self, k=10) -> list:
        area_tree = self.test_init_area_data()

        ret_list = []
        for i in range(k):
            p = area_tree[k % len(area_tree)]
            city_vo = p.children[k % len(p.children)]
            c_vo = city_vo.children[k % len(city_vo.children)]
            address = Address(province=p.area_name, city=city_vo.area_name, county=c_vo.area_name,
                              info="详细地址_" + str(i))
            ret_list.append(address)
        return ret_list

    def test_init_user_data(self):
        length = 3
        address_list = self.test_init_address_data(length)
        ret_user_list = []
        for i in range(length):
            user = User(name="测试用户" + str(i),
                        birth_day=date.today(),
                        address_list=[address_list[i], address_list[(i + 1) % length]])
            ret_user_list.append(user)
        return ret_user_list

    def test_to_yaml(self):
        data_list = self.test_init_user_data()
        # data = [o.__dict__ for o in data_list]
        FileUtil.to_yaml(data_list, get_data_dir("to_yaml.yaml"))

    def test_from_yaml(self):
        data = FileUtil.from_yaml(get_data_dir("to_yaml.yaml"))
        print(data)

    def test_to_prop(self):
        # data_list = self.test_init_user_data()
        data = {'name': '测试用户0', 'birth_day': "2022-10-10", 'address': {"city": 1}}
        FileUtil.to_prop(data, get_data_dir("to_prop.application"))

    def test_from_prop(self):
        data = FileUtil.from_prop(get_data_dir("to_prop.application"))
        print(data)

    def test_to_xmind(self):
        data_list = self.test_init_area_data()
        data = class_dict_util.class_to_dict(data_list)
        FileUtil.to_xmind(data, get_data_dir("to_xmind.yaml"), key="area_name")

    def test_from_xmind(self):
        data = FileUtil.from_xmind(get_data_dir("to_xmind.yaml"))
        print(data)
