
import unittest

import schedule


class Pc(unittest.TestCase):
    def test1(self):
        schedule.every(2).seconds.do(Pc.job)  # 每10秒执行一次
        while True:
            schedule.run_pending()

    @staticmethod
    def job():
        print("I'm working...")
