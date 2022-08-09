from datetime import date
from unittest import TestCase

from util.cache_util import to_file


class User:
    def __init__(self, name=None, birth_day=None, address=None):
        self.name = name
        self.birth_day = birth_day
        self.address = address


class Address:
    def __init__(self, 省=None, 市=None, 区=None, info=None, ):
        self.省 = 省
        self.市 = 市
        self.区 = 区
        self.info = info


class Area:
    def __init__(self, area_name=None):
        self.area_name = area_name
        self.children = []


class TestAutoCode(TestCase):

    @to_file("area.json")  # TypeError: Object of type Area is not JSON serializable
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

    def test_init_address_data(self):
        area_tree = self.test_init_area_data()

        for i in range(9):
            Address(省=1)
            User(name="测试用户" + str(i), birth_day=date.today(), )

    def test_init_user_data(self):
        for i in range(3):
            User(name="测试用户" + str(i), birth_day=date.today(), )


if __name__ == '__main__':
    TestAutoCode().test_init_area_data()
