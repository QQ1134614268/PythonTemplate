import unittest

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone


class TestScheduleAsp(unittest.TestCase):
    def test1(self):
        executors = {
            'default': ThreadPoolExecutor(10),
            'processpool': ProcessPoolExecutor(3)
        }
        job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }

        # 实例调度器对象
        scheduler = BlockingScheduler(executors=executors, job_defaults=job_defaults,
                                      timezone=timezone('Asia/Shanghai'))
        # 每分钟第30秒执行一次 # trigger = ``date``, ``interval`` or ``cron``
        scheduler.add_job(func=TestScheduleAsp.job, trigger=CronTrigger(second=30))

        print("crontab run~")
        scheduler.start()

    @staticmethod
    def job():
        print("I'm working...")

    @staticmethod
    def job2():
        #  拦截器
        print("I'm working...")
