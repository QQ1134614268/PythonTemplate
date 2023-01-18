# 设置 test runner

# unittest mock pytest nose2
# todo 数据驱动模块 parameterized ddt; pytest 自动支持; mock
import pytest as pytest
import unittest


# 示例：
# 首先，我们观察这三个测试用例，我们会发现，三个测试用例除了入口参数需要变化，
# 其测试执行语句都是相同的，因此，为了简化测试代码，我们可以使用数据驱动测试的理论将三个方法写作一个方法

# 未使用数据驱动测试的代码：
class BasicTestCase(unittest.TestCase):
    def test1(self, num1):
        num = num1 + 1
        # self.assertEqual(8, num)
        print('number:', num)

    def test2(self, num2):
        num = num2 + 1
        print('number:', num)

    def test3(self, num3):
        num = num3 + 1
        print('number:', num)


# # 使用数据驱动测试的代码，执行效果与上文代码相同此处只需要了解大概框架，详细步骤下文会解释
# @ddt
# class BasicTestCase(unittest.TestCase):
#     @data('666', '777', '888')
#     def test(self, num):
#         print('数据驱动的number:', num)


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

    # assertEqual、assertNotEqual、assertTrue、assertFalse、assertIn、assertNotIn 等。


# w1.py
def weather():
    '''天气接口'''
    pass


def weather_result():
    '''模拟天气接口返回值'''
    result = weather()
    if result['result'] == '雪':
        print('下雪了！！！')
    elif result['result'] == '雨':
        print('下雨了！！！')
    elif result['result'] == '晴天':
        print('晴天！！！！')
    else:
        print('返回值错误！')
    return result['status']


import unittest
from unittest import mock


# 导入接口文件


# class Test01(unittest.TestCase):
#
#     @mock.patch(target="weather")
#     def test_01(self, mock_login):
#         '''下雪了'''
#         mock_login.return_value = {'result': "雪", 'status': '下雪了！'}
#         statues = weather()
#         self.assertEqual(statues, '下雪了！')
#
#     @mock.patch(target='weather')
#     def test_02(self, mock_login):
#         '''下雨了！'''
#         mock_login.return_value = {'result': "雨", 'status': '下雨了！'}
#         statues = weather()
#         self.assertEqual(statues, '下雨了！')


if __name__ == '__main__':
    unittest.main()
