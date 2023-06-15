import time
import unittest


class TestYield(unittest.TestCase):
    def test_yield(self):
        def fun():
            a = (yield 1 + 1)
            print("a = ", a)
            b = yield a
            print("b = ", b)
            c = yield b
            print("c = ", c)

        x = fun()  # x 是一个生成器
        print(x.__next__())  # 程序运行到yield就停住了,等待下一个next
        print(x.send(4))  # 我们给yield发送值1,然后这个值被赋值给了b，并且打印出来,然后继续下一次循环停在yield处
        print(x.send(5))

    def test_yield2(self):
        def fun():
            a = yield 1
            print("a = ", a)
            b = yield a
            print("b = ", b)

        x = fun()
        print(x.__next__())
        print(x.send(4))
        print(x.send(5))

    def test_fib(self):
        def fib(num):
            n = 0
            a, b = 0, 1
            while n < num:
                yield b
                a, b = b, a + b
                n = n + 1

        a = fib(30)
        for i in a:
            print(i)

        a = fib(30)
        print(next(a), next(a), next(a), next(a))  # 1 1 2 3
        a.close()

        a = fib(30)
        print(a.__next__(), a.__next__(), a.__next__(), a.__next__())  # 1 1 2 3
        a.close()

    def test_corn(self):

        def consume():
            r = ''
            while True:
                n = yield r
                if not n:
                    return
                print('[consumer] consuming %s...' % n)
                time.sleep(1)
                r = 'well received'

        def produce(num):
            next(num)
            n = 0
            while n < 5:
                n = n + 1
                print('[producer] producing %s...' % n)
                r = num.send(n)
                print('[producer] consumer return: %s' % r)
            num.close()

        c = consume()
        produce(c)
