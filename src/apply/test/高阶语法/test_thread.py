import unittest
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread


class TestThread(unittest.TestCase):
    @staticmethod
    def test_a(name, value2=None):
        print('hello', name, f"value2: {value2}")

    def test_thread(self):
        thr = Thread(target=self.test_a, args="tom", kwargs={})
        thr.start()

    def test_thread_pool(self):
        thread_pool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
        for i in range(0, 10):
            future = thread_pool.submit(self.test_a, "tom", i)
            # print(future.result())
        thread_pool.shutdown(wait=True)
