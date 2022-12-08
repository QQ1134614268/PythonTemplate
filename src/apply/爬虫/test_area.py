import time
from unittest import TestCase

import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class Area(Base):
    __tablename__ = 'area'
    id = Column(INTEGER, primary_key=True, comment="id")
    area_name = Column(String(64), index=True, comment="名称")
    parent_id = Column(INTEGER, index=True, comment="父级id")


class Test(TestCase):
    def test_pre(self):
        ...
        # Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test_main(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2021/'

        trs = self.get_response(base_url, 'provincetr')
        for tr in trs:  # 循环每一行
            datas = []
            for td in tr:  # 循环每个省
                province_name = td.a.get_text()
                province_url = base_url + td.a.get('href')
                province_vo = Area(area_name=province_name)
                localhost_test_session.add(province_vo)
                localhost_test_session.commit()
                trs = self.get_response(province_url, None)
                for tr in trs[1:]:  # 循环每个市
                    city_code = tr.find_all('td')[0].string
                    city_name = tr.find_all('td')[1].string
                    city_url = base_url + tr.find_all('td')[1].a.get('href')
                    trs = self.get_response(city_url, None)
                    city_vo = Area(area_name=str(city_name), parent_id=province_vo.id)
                    localhost_test_session.add(city_vo)
                    localhost_test_session.commit()
                    for tr in trs[1:]:  # 循环每个区
                        county_code = tr.find_all('td')[0].string
                        county_name = tr.find_all('td')[1].string
                        data = [province_name, city_code, city_name, county_code, county_name]
                        county_vo = Area(area_name=str(county_name), parent_id=city_vo.id)
                        localhost_test_session.add(county_vo)
                        localhost_test_session.commit()
                        datas.append(data)
                    time.sleep(1)

    def get_response(self, url, attr):
        response = requests.get(url)
        response.encoding = 'utf-8'  # 编码转换
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find_all('tbody')[1].tbody.tbody.table
        if attr:
            trs = table.find_all('tr', attrs={'class': attr})
        else:
            trs = table.find_all('tr')
        return trs
