# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import re
import unittest
from datetime import datetime, timedelta
from typing import List
from xml.etree import ElementTree

from sqlalchemy import Column, Integer, String, DateTime, func, Text, JSON
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class CameraLog(Base):
    __tablename__ = 'camera_log'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    ip = Column(String(64), comment="ip")
    xml_txt = Column(Text, comment="xml内容")
    report_time = Column(DateTime, comment="上报时间")


class CameraEvent(Base):
    __tablename__ = 'camera_event'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    topic = Column(String(64), comment="topic")
    time = Column(DateTime, comment="预警时间")
    data = Column(JSON, comment="上报时间")
    camera_log_id = Column(Integer, comment="camera_log表id")
    ip = Column(String(64), comment="ip")
    report_time = Column(DateTime, comment="上报时间")


class TestCameraEvent(unittest.TestCase):
    def test_pre(self):
        ...
        Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test_xml_db(self):
        max_time = localhost_test_session.query(func.max(CameraLog.report_time)).scalar()

        res_list = []
        with open(r"C:\Users\Administrator\Desktop\xc-ship.log", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if "预警-内容:" not in line:
                    continue
                arr = re.split("预警: ip:| 预警-内容: ", line)
                date_str = re.search(r'UtcTime.*?"(.*?)T', line).groups()[0]
                time_str = re.search(r'(.{8})', line).groups()[0]
                report_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
                if not max_time or report_time > max_time:
                    res_list.append(CameraLog(ip=arr[1], xml_txt=arr[2], report_time=report_time))
        if res_list:
            localhost_test_session.add_all(res_list)
            localhost_test_session.commit()
        print(f"---------{len(res_list)}--------------")

        # 日志分析
        max_time = localhost_test_session.query(func.max(CameraEvent.time)).scalar()
        max_id = localhost_test_session.query(func.max(CameraEvent.camera_log_id)).scalar() or 0
        camera_log_vos: List[CameraLog] = localhost_test_session.query(CameraLog).filter(CameraLog.id > max_id).all()

        res_list = []
        for vo in camera_log_vos:
            new1 = re.sub(r"(<\w*?:)", "<", vo.xml_txt)
            new2 = re.sub(r"(</\w*?:)", "</", new1)
            envelop_ele = ElementTree.XML(new2)
            body_ele = envelop_ele.find('Body')
            notify_ele = body_ele.find('Notify')
            notify_meg_ele_list = notify_ele.findall('NotificationMessage')
            for notify_meg_ele in list(notify_meg_ele_list):
                topic_ele = notify_meg_ele.find('Topic')
                topic = topic_ele.text
                message_ele = notify_meg_ele.find('Message')
                message_ele_list = message_ele.findall('Message')
                for message_ele in list(message_ele_list):
                    data = {"source": [], "data": [], "key": [], }
                    utc_time = message_ele.attrib.get("UtcTime")
                    time = datetime.strptime(utc_time, "%Y-%m-%dT%H:%M:%SZ") + timedelta(hours=8)

                    source_ele = message_ele.find("Source")
                    if source_ele:
                        for item in list(source_ele.findall("SimpleItem")):
                            data.get("source").append(item.attrib)

                    data_ele = message_ele.find("Data")
                    if data_ele:
                        for item in list(data_ele.findall("SimpleItem")):
                            data.get("data").append(item.attrib)

                    key_ele = message_ele.find("Key")
                    if key_ele:
                        for item in list(key_ele.findall("SimpleItem")):
                            data.get("key").append(item.attrib)
                    if not max_time or time > max_time:
                        res_list.append(
                            CameraEvent(topic=topic, time=time, data=data, ip=vo.ip,
                                        camera_log_id=vo.id, report_time=vo.report_time))
        if res_list:
            localhost_test_session.add_all(res_list)
            localhost_test_session.commit()
        print(f"---------{len(res_list)}--------------")
