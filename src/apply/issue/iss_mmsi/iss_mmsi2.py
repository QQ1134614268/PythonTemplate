import json
import re
import time
from typing import List
from unittest import TestCase

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from sqlalchemy import Column, String, Text, Float
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class Mmsi(Base):
    __tablename__ = 'mmsi'
    id = Column(INTEGER, primary_key=True, comment="id")
    mmsi = Column(String(64), index=True, unique=True, comment="mmsi")
    data = Column(Text, comment="返回结果")


class Mmsi2(Base):
    __tablename__ = 'mmsi2'
    id = Column(INTEGER, primary_key=True, comment="id")
    mmsi = Column(String(64), index=True, unique=True, comment="mmsi")
    data = Column(Text, comment="返回结果")
    data_name = Column(Text, comment="返回结果")
    data_table = Column(Text, comment="返回结果")


class Mmsi3(Base):
    __tablename__ = 'mmsi3'
    id = Column(INTEGER, primary_key=True, comment="id")
    source = Column(INTEGER, comment="source")
    mmsi = Column(String(64), index=True, comment="mmsi")  # unique=True,
    shipid = Column(Text, comment="返回结果")
    tradetype = Column(INTEGER, comment="返回结果")
    type = Column(INTEGER, comment="类型")
    name = Column(Text, comment="imo")
    cnname = Column(Text, comment="imo")
    imo = Column(Text, comment="imo")
    matchtype = Column(INTEGER, comment="imo")
    callsign = Column(Text, comment="呼号")
    length = Column(Float(precision=23), comment="船长（米）")
    width = Column(Float(precision=23), comment="船宽（米）")
    left = Column(INTEGER, comment="船宽（米）")
    trail = Column(INTEGER, comment="船宽（米）")
    draught = Column(Float(precision=23), comment="吃水")
    dest = Column(Text, comment="目的地")
    eta = Column(Text, comment="预计到达时间")
    lon = Column(INTEGER, comment="经度")
    lat = Column(INTEGER, comment="纬度")
    sog = Column(INTEGER, comment="对地航速")
    cog = Column(INTEGER, comment="对地航向")
    hdg = Column(INTEGER, comment="船首向")
    rot = Column(INTEGER, comment="雷达仅战术")
    navistatus = Column(INTEGER, comment="船宽（米）")
    laststa = Column(INTEGER, comment="船宽（米）")
    lastdyn = Column(INTEGER, comment="船宽（米）")
    satelliteutc = Column(INTEGER, comment="船宽（米）")


class TestMmsi(TestCase):
    def test_pre(self):
        ...
        # Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test_main(self):
        browser = WebDriver(service=Service(executable_path='chromedriver.exe'))
        browser.maximize_window()  # 窗口最大化
        browser.get('https://www.shipxy.com/')

        with open("mmsi.txt", mode='r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '').replace('\r', '')
            if len(line) != 9:
                continue
            if localhost_test_session.query(Mmsi2).filter(Mmsi2.mmsi == line).all():
                continue
            vo1: Mmsi = localhost_test_session.query(Mmsi).filter(Mmsi.mmsi == line).first()
            if vo1:
                txt = vo1.data
                localhost_test_session.add(Mmsi2(mmsi=line, data=txt))
                localhost_test_session.commit()
                continue
            try:
                browser.find_element(By.ID, 'txtKey').clear()
                browser.find_element(By.ID, 'txtKey').send_keys(line)  # 413871643 215748000
                element = browser.find_element(By.ID, 'searchBtn')
                element.click()
                time.sleep(1)

                element = browser.find_element(By.ID, 'si_name_ext')
                name_cn = element.text
                element = browser.find_element(By.ID, 'si_name')
                name_en = element.text
                element = browser.find_element(By.ID, 'shipAIS')
                table = element.text
                time.sleep(1)
                element = browser.find_element(By.XPATH, '//*[@id="shipinfoTitle"]/div[1]/a')
                element.click()

                localhost_test_session.add(Mmsi2(mmsi=line, data_name=name_cn + name_en, data_table=table))
                localhost_test_session.commit()
            except Exception as e:
                print(e)
                localhost_test_session.add(Mmsi2(mmsi=line, data="00"))
                localhost_test_session.commit()

    def test_main2(self):
        self.test_pre()
        localhost_test_session.query(Mmsi3).delete()
        res = []
        vos: List[Mmsi2] = localhost_test_session.query(Mmsi2).all()
        for vo in vos:
            if vo.data == '00':
                # res.append({
                #     'mmsi': vo.mmsi,
                # })
                continue
            if vo.data:
                res1 = json.loads(vo.data)
                data = res1["data"] and res1["data"][0]
                if data:
                    res.append({
                        'mmsi': data['mmsi'],
                        'name': data['name'],
                        'cnname': data['cnname'],
                        'length': data['length'],
                        'width': data['width'],
                        'draught': data['draught'],
                        'callsign': data['callsign'],
                        'imo': data['imo'],
                    })

            if vo.data_table:
                names = str(vo.data_name).split(" -")
                name = names[-1]
                cnname = len(names) == 2 and names[0] or None

                info = vo.data_table
                match = re.search(r"(MMSI： )([0-9]+)", info)
                mmsi = match and match.groups()[1] or vo.mmsi
                match = re.search(r"(呼号： )([a-zA-Z0-9]+)", info)
                callsign = match and match.groups()[1] or None
                match = re.search(r"(IMO： )(\w+)", info)
                imo = match and match.groups()[1] or None
                # match = re.search(r"(类型： )(\w+)", info)
                # callassign = match or match.groups()[1]
                match = re.search(r"(船长： )(\w+)(米)", info)
                length = match and match.groups()[1] or None
                match = re.search(r"(船宽： )(\w+)(米)", info)
                width = match and match.groups()[1] or None
                match = re.search(r"(吃水： )(\w+)(米)", info)
                draught = match and match.groups()[1] or None
                res.append({
                    'mmsi': mmsi,
                    'name': name,
                    'cnname': cnname,
                    'length': length,
                    'width': width,
                    'draught': draught,
                    'callsign': callsign,
                    'imo': imo,
                })

        localhost_test_session.add_all([Mmsi3(**dic) for dic in res])
        localhost_test_session.commit()
        print("---------- OVER -----------")
