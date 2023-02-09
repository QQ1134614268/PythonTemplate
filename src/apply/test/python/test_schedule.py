
import unittest

import schedule


class TestSchedule(unittest.TestCase):
    def test1(self):
        schedule.every(2).seconds.do(TestSchedule.job)  # 每10秒执行一次

        # schedule.every(5).minutes.do(job, name)
        # schedule.every().hour.do(job, name)
        # schedule.every().day.at("10:30").do(job, name)
        # schedule.every(5).to(10).days.do(job, name)
        # schedule.every().monday.do(job, name)
        # schedule.every().wednesday.at("13:15").do(job, name)

        while True:
            schedule.run_pending()

    @staticmethod
    def job():
        print("I'm working...")
