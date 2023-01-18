import datetime
from unittest import TestCase

from sqlalchemy import Column, Date
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class Calendar(Base):
    __tablename__ = 'calendar'
    date = Column(Date, primary_key=True, comment="日期")
    year = Column(INTEGER, comment="年")
    month = Column(INTEGER, comment="月")
    day = Column(INTEGER, comment="日")
    week = Column(INTEGER, comment="周")
    week_year = Column(INTEGER, comment="一年第几周")
    quarter = Column(INTEGER, comment="季度")
    half_year = Column(INTEGER, comment="半年")


class Test(TestCase):
    def test_pre(self):
        ...
        Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test_main(self):
        self.test_pre()

        year = 100
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020 + year, 1, 1)
        dlt = end_date - start_date

        cur_date = start_date
        next_day = datetime.timedelta(days=1)
        day_list = []
        for i in range(dlt.days):
            week = cur_date.weekday() + 1
            week_year = cur_date.isocalendar()[1]
            quarter = cur_date.month // 3 + 1
            half_year = quarter // 2 + 1
            vo = Calendar(date=cur_date, year=cur_date.year, month=cur_date.month, day=cur_date.day, week=week,
                          week_year=week_year, quarter=quarter, half_year=half_year)
            day_list.append(vo)
            if len(day_list) > 1000:
                self.save_all(day_list)
            cur_date += next_day
        if len(day_list) > 0:
            self.save_all(day_list)

    @staticmethod
    def save_all(day_list):
        localhost_test_session.add_all(day_list)
        localhost_test_session.commit()
        day_list.clear()
