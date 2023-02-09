import time
from datetime import datetime

import psutil
import unittest

import schedule as schedule

from apply.test.test_pc_info.model import Base, PidInfo, NetInfo
from config.db_conf import localhost_test_engine, localhost_test_session


class TestPsutil(unittest.TestCase):
    def test_init_table(self):
        Base.metadata.create_all(localhost_test_engine)
        # Base.metadata.drop_all(localhost_test_engine)

    def test1(self):
        name = "longsongpong"
        schedule.every(5).minutes.do(Pc.test1_get_info, name)
        # schedule.every().hour.do(job, name)
        # schedule.every().day.at("10:30").do(job, name)
        # schedule.every(5).to(10).days.do(job, name)
        # schedule.every().monday.do(job, name)
        # schedule.every().wednesday.at("13:15").do(job, name)

        while True:
            schedule.run_pending()
            time.sleep(30)

    def test1_get_info(self):
        time = datetime.now()
        # pids = psutil.pids()
        # psutil.process_iter()
        process_list = []
        for process in psutil.process_iter():
            try:
                cmdline = " ".join(process.cmdline())
            except psutil.AccessDenied as e:
                print(e)
            process_list.append(PidInfo(
                pid=process.pid, cmdline=cmdline, create_time=time,
            ))

        localhost_test_session.add_all(process_list)

        net_list = []
        for net_info in psutil.net_connections():
            laddr, raddr = "", ""
            try:
                laddr = f"{net_info.laddr.ip}:{net_info.laddr.port}"
                raddr = f"{net_info.raddr.ip}:{net_info.raddr.port}"
            except Exception as e:
                print(e)

            net_list.append(
                NetInfo(
                    pid=net_info.pid,
                    laddr=laddr,
                    raddr=raddr,
                    create_time=time,
                )
            )

        localhost_test_session.add_all(net_list)
        localhost_test_session.commit()
