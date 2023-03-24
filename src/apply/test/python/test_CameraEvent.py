# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import datetime
import json
import unittest
import uuid
import xml

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

server_240_out_log = "out.log"

dev_desktop_out_log = r"C:\Users\Administrator\Desktop\out.log"

Base = declarative_base()


class CameraEvent(Base):
    __tablename__ = 'camera_event'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    batch_id = Column(String(64), comment="批量id")
    current_time = Column(DateTime, comment="当前时间")
    termination_time = Column(DateTime, comment="时间")
    topic = Column(String(64), comment="topic")
    name = Column(String(64), comment="名称")
    value = Column(String(64), comment="值")
    time = Column(DateTime, comment="预警时间")
    channel = Column(String(64), comment="通道")


class TestCameraEvent(unittest.TestCase):
    def test_pre(self):
        ...
        Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test_fmt_file(self):
        with open("out2.log", mode="w") as f2:
            with open(dev_desktop_out_log, encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    data = json.loads(line)
                    f2.write(json.dumps(data) + "\n")

    def test_to_db(self):
        max_time = localhost_test_session.query(func.max(CameraEvent.time)).scalar()

        res_list = []
        with open(dev_desktop_out_log, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                data = json.loads(line)
                _id = str(uuid.uuid1())
                params = data["params"]
                events = params["events"]
                for e in events:
                    for v in e["value"]:
                        v["topic"] = e["topic"]
                        v["current_time"] = datetime.datetime.fromtimestamp(params["current_time"])
                        # datetime.datetime.fromtimestamp()
                        # time.localtime(params["current_time"])
                        # datetime.datetime. params["current_time"] * 1000
                        v["termination_time"] = datetime.datetime.fromtimestamp(params["termination_time"])
                        # params["termination_time"] * 1000
                        v["batch_id"] = _id
                        v["time"] = datetime.datetime.fromtimestamp(v["time"])
                        if not max_time or v["time"] > max_time:
                            res_list.append(CameraEvent(**v))
        self.save_all(res_list)

    @staticmethod
    def save_all(day_list):
        if day_list:
            day_list.sort(key=lambda x: x.time)
            # day_list = sorted(day_list, key=lambda x: x.time)
            localhost_test_session.add_all(day_list)
            localhost_test_session.commit()
        print(f"---------{len(day_list)}--------------")

    def test_server_filter_01(self):
        str_flag = "预警内容:"
        dir_path = ""
        files = []
        with open(server_240_out_log, mode="w") as f2:
            for file in files:
                with open(file, encoding="utf-8") as f:
                    for line in f.readlines():
                        if str_flag in line:
                            f2.write(line.split(str_flag)[-1] + "\n")

    def test_xml(self):
        pass
        xml
