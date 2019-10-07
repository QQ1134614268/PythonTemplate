# coding=utf-8
import unittest


# 被测试方法
def cal(a, b):
    return a + b


# 测试类
class CalTest(unittest.TestCase):
    def testA(self):
        expected = 6
        result = cal(2, 4)
        self.assertEqual(expected, result)

    def testB(self):
        expected = 0
        result = cal(2, 1)
        self.assertEqual(expected, result)


# 执行所以测试代码
if __name__ == '__main__':
    unittest.main()
