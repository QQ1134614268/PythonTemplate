import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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


class Mmsi2(Base):
    __tablename__ = 'mmsi2'
    id = Column(INTEGER, primary_key=True, comment="id")
    mmsi = Column(String(64), index=True, unique=True, comment="mmsi")
    data = Column(Text, comment="返回结果")
    data_name = Column(Text, comment="返回结果")
    data_table = Column(Text, comment="返回结果")


class TestMmsi(TestCase):
    def test_pre(self):
        ...
        # Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test_main(self):
        option = Options()
        browser = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
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
