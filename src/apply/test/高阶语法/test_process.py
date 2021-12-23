import unittest
from multiprocessing import Process, Pool


class TestProcess(unittest.TestCase):

    @staticmethod
    def test_a(name):
        print('hello', name)

    def test_process(self):
        p = Process(target=self.test_a, args=('bob',))
        p.start()
        p.join()

    def test_process_pool(self):
        with Pool(5) as p:
            print(p.map(self.test_a, [1, 2, 3]))
