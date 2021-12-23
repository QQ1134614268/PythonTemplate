import unittest


def fib(num):
    n = 0
    a, b = 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1


def test_2(num):
    while True:
        msg = yield num + 1  # yield b 赋值给msg，msg接收send来的信号。
        print("接收:", msg)


class TestMysql(unittest.TestCase):
    def test_for(self):
        a = fib(30)
        for i in a:
            print(i)

    def test_next(self):
        a = fib(30)
        print(next(a), next(a), next(a), next(a))  # 1 1 2 3
        a.close()

    def test__next__(self):
        a = fib(30)
        print(a.__next__(), a.__next__(), a.__next__(), a.__next__())  # 1 1 2 3
        a.close()

    def test_send(self):
        # next：唤醒并继续执行
        # send：唤醒并继续执行
        # 　　　发送信息到生成器内部。
        a = test_2(5)
        print(next(a), next(a))
        print("-------------")
        a.send(10)
        print(next(a), next(a))

        # 接收: None
        # 6 6
        # -------------
        # 接收: 10
        # 接收: None
        # 接收: None
        # 6 6
