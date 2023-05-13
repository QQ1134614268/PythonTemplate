# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import json
import unittest
import uuid
from datetime import datetime
from xml.etree import ElementTree

from sqlalchemy import Column, Integer, String, DateTime, func, Text
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class CameraLog(Base):
    __tablename__ = 'camera_log'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    channel_no = Column(String(64), comment="通道")
    xml_txt = Column(Text, comment="通道")
    report_time = Column(Text, comment="上报时间")


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

    def test_to_db(self):
        max_time = localhost_test_session.query(func.max(CameraEvent.time)).scalar()

        res_list = []
        with open(r"C:\Users\Administrator\Desktop\out.log", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                data = json.loads(line)
                _id = str(uuid.uuid1())
                params = data["params"]
                events = params["events"]
                for e in events:
                    for v in e["value"]:
                        v["topic"] = e["topic"]
                        v["current_time"] = datetime.fromtimestamp(params["current_time"])
                        # time.localtime(params["current_time"])
                        # datetime. params["current_time"] * 1000
                        v["termination_time"] = datetime.fromtimestamp(params["termination_time"])
                        # params["termination_time"] * 1000
                        v["batch_id"] = _id
                        v["time"] = datetime.fromtimestamp(v["time"])
                        if not max_time or v["time"] > max_time:
                            res_list.append(CameraEvent(**v))
        self.save_all(res_list)

    def test_to_db2(self):
        max_time = localhost_test_session.query(func.max(CameraEvent.time)).scalar()

        res_list = []
        with open("C:\\Users\\Administrator\\Desktop\\out.json.log", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    _id = str(uuid.uuid1())
                    notification_message = data.get("body", {}).get("notificationMessage", [])
                    for messageItem in notification_message:
                        topic = messageItem.get("topic", {}).get("value")
                        for item in messageItem.get("message", []):
                            utc_time = datetime.strptime(item.get("utcTime"), "%Y-%m-%dT%H:%M:%SZ")
                            for item2 in item.get("source", {}).get("simpleItem", []):
                                if not max_time or utc_time > max_time:
                                    res_list.append(
                                        CameraEvent(
                                            topic=topic,
                                            batch_id=_id,
                                            time=utc_time,
                                            name=item2.get("name"),
                                            value=item2.get("value"),
                                            channel=item2.get("value", "-")[-1:]
                                        )
                                    )

                except Exception as e:
                    print(line)
                    print(e)

        self.save_all(res_list)

    @staticmethod
    def save_all(day_list):
        if day_list:
            day_list.sort(key=lambda x: x.time)
            # day_list = sorted(day_list, key=lambda x: x.time)
            localhost_test_session.add_all(day_list)
            localhost_test_session.commit()
        print(f"---------{len(day_list)}--------------")

    def test_xml(self):
        with open("C:\\Users\\Administrator\\Desktop\\out.xml.log", mode="r") as f2:
            for line in f2.readlines():
                with open("tmp.xml", mode="w") as f3:
                    f3.write(line)
                tree = ElementTree.parse("tmp.xml")
                root = tree.getroot()
                print(tree, root, root.tag, root.attrib, root.text, root.tail, root.getchildren())

