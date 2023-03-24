import unittest
from unittest import mock

from ddt import ddt, data, unpack


# unittest 组织成类, 自带的, 被(pytest)拓展
# pytest 支持数据驱动?? 插件丰富(生成报告,发邮件)
# ddt 配合unittest, 数据驱动

# todo 个人使用 unittest,配合ddt??

# pycharm 设置 test runner
@ddt  # ddt是用来装饰类的，需要与data装饰器一起使用
class TestDdt(unittest.TestCase):

    @staticmethod
    def add(num1, num3):
        return num1 + num3

    def test(self):
        """没有数据驱动的测试"""
        assert self.add(1, 2), 3
        assert self.add(1, -2), -1

    @data('666', '777', '888')
    def test1(self, num):
        res = str(num)
        print('数据驱动的number:', res)

    @data([1, 2], [1, -2])
    @unpack
    def test_add(self, num1, num2):
        assert self.add(num1, num2), 3
        assert self.add(1, -2), -1

    @mock.patch(target="test_ddt.add")
    def test_01(self, mock_add):
        # mock: 调用mock的方法只返回给定的值
        mock_add.return_value = 2

        statues = add(100, 200)
        self.assertEqual(statues, 2)


def add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    # 运行的时候光标的位置放在 test_add 方法中了，导入且使用ddt后，运行时需要先识别装饰的类，将光标放在方法内的话，测试用例仅会执行当前的方法，ddt无法识别到类，运行就会出错。

    # 将光标放到方法外，则运行通过；
    # 加main方法，再运行，也会运行通过；
    # 点击py文件，右击运行，也会运行通过
    unittest.main()
