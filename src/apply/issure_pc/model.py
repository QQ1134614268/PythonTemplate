from datetime import datetime

from sqlalchemy import Column, Enum, MetaData, String, Text, PrimaryKeyConstraint, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseTable(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="修改时间")
    create_by = Column(Integer, default="-1", comment="创建者id")
    update_by = Column(Integer, default="-1", comment="修改者id")


class PidInfo(BaseTable):
    __tablename__ = 'pid_info'
    pid = Column(String(64))
    cmdline = Column(Text)


class NetInfo(BaseTable):
    __tablename__ = 'net_info'
    pid = Column(String(64))
    laddr = Column(Text)
    raddr = Column(Text)
