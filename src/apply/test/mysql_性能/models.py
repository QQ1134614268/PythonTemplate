import datetime

from sqlalchemy import Column, DateTime, Integer, Float
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BaseTable(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment="修改时间")
    create_by = Column(Integer, default="-1", comment="创建者id")
    update_by = Column(Integer, default="-1", comment="修改者id")


class User(BaseTable):
    __tablename__ = 'performance_user_t'
    __table_args__ = (
        # Index('name', unique=True),
        {'comment': '用户表'},
    )
    name = Column(VARCHAR(20), comment='姓名')
    sex = Column(Integer, comment='性别')


class Order(BaseTable):
    __tablename__ = 'performance_order_t'
    __table_args__ = (
        {'comment': '用户表'},
    )
    user_id = Column(Integer, comment='客户id')
    status = Column(VARCHAR(20), comment='订单状态')


class OrderInfo(BaseTable):
    __tablename__ = 'performance_order_info_t'
    __table_args__ = (
        {'comment': '订单详情'},
    )
    order_id = Column(Integer, comment='订单id')

    price = Column(Float(10, 4), comment='价格')
    num = Column(Integer, comment='数量')
    goods_id = Column(Integer, comment='商品id')
    goods_name = Column(VARCHAR(20), comment='商品名')


class Goods(BaseTable):
    __tablename__ = 'performance_goods_t'
    __table_args__ = (
        {'comment': '商品表'},
    )
    num = Column(Integer, comment='库存')
    goods_name = Column(VARCHAR(20), comment='商品名')
