import json
import threading
from queue import Queue
from unittest import TestCase

import requests
import time
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class Mmsi(Base):
    __tablename__ = 'mmsi'
    id = Column(INTEGER, primary_key=True, comment="id")
    mmsi = Column(String(64), index=True, unique=True, comment="mmsi")
    data = Column(Text, comment="返回结果")


class TestMmsi(TestCase):
    def test_pre(self):
        ...
        # Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test_init_mmsi(self):
        data = []
        with open("mmsi.txt", encoding="utf-8", mode="r") as f:
            for line in f.readlines():
                mmsi = line.replace("\r", "").replace("\n", "")
                if mmsi:
                    data.append(mmsi)

        data = list([Mmsi(mmsi=line.replace("\r", "").replace("\n", "")) for line in sorted(list(set(data)))])
        localhost_test_session.add_all(data)
        localhost_test_session.commit()
        print(f"---{len(data)}---")

    def test_main(self):
        vos = localhost_test_session.query(Mmsi).filter(
            Mmsi.data.isnot(None)
        ).all()
        task = Queue()
        for vo in vos:
            task.put(vo)

        # todo 保存报错,, session多线程不安全??

        # todo 队列, 线程分布式
        t = []
        for i in range(16):
            t1 = threading.Thread(target=self.for_que, args=(task,))
            t.append(t1)
        for i in t:
            i.start()
        while True:
            time.sleep(0.1)

    def test_main2(self):
        # vos = localhost_test_session.query(Mmsi).filter(Mmsi.data.is_(None)).all()
        vos = localhost_test_session.query(Mmsi).filter(Mmsi.data == '{"status":0,"data":[]}').all()

        for vo in vos:
            vo.data = self.test_get_mmsi(vo.mmsi)
            localhost_test_session.commit()

    def test_result(self):
        vos = localhost_test_session.query(Mmsi).filter(Mmsi.data != '{"status":0,"data":[]}').all()
        data = [vo.data for vo in vos]
        with open("mmsi.out.log", encoding="utf-8", mode="w") as f:
            f.write("\n".join(data))

    def for_que(self, que: Queue):
        arg = que.get()
        if not arg:
            return
        data = TestMmsi.test_get_mmsi(arg.mmsi)
        localhost_test_session.query(Mmsi).filter(Mmsi.id == arg.id).update({'data': data})
        localhost_test_session.commit()
        self.for_que(que)

    @staticmethod
    def test_get_mmsi(mmsi):
        # time.sleep(random.randint(3, 6))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
        }
        try:
            rq2 = requests.post(
                "https://www.shipxy.com/ship/GetShip",
                data={
                    'mmsi': mmsi,
                    # "shipIDs": mmsi
                },
                headers=headers)
            if rq2.status_code == 200:
                # result2 = json.loads(rq2.text)
                # print(result2)
                return rq2.text
            else:
                print(json.dumps(rq2))
                return json.dumps(rq2)
        except:
            print(mmsi)
