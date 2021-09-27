# -*- coding:utf-8 -*-
"""
@Time: 2021/8/24
@Description:
"""
import datetime

from sqlalchemy import Column, DateTime, Date, String, DECIMAL, Integer, UniqueConstraint, func, create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RightManage(Base):
    # 表名称
    __tablename__ = 'right_manage'
    __table_args__ = {
        'mysql_engine': "InnoDB",
        'mysql_collate': 'utf8mb4_general_ci',
        'mysql_charset': 'utf8mb4',
        'comment': '权益管理',
    }
    # 表结构
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    biz_date = Column(Integer, comment="操作日期")
    board = Column(String(64), comment="股票,基金,债券")
    market = Column(String(64), comment="市场")
    stk_code = Column(String(64), comment="证券代码")
    right_type = Column(String(64), comment="0:红利,1:红股,2:可转债权益,3:增发权益,4:配股权益")
    stk_short_name = Column(String(64), comment="证券简称")
    anno_date = Column(Date, comment="公告日")

    share_plan = Column(String(64), comment="分配方案")
    bonus_type = Column(String(64), comment="权益类别")
    target_market = Column(String(64), comment="目标市场")
    target_code = Column(String(64), comment="目标代码")

    wind_register_date = Column(Date, comment="WIND-登记日")
    wind_except_date = Column(Date, comment="WIND-除权日")
    wind_receipt_date = Column(Date, comment="WIND-到账日")
    wind_cash_per_share = Column(DECIMAL(20, 8), comment="WIND-每股派现金")
    wind_bonus_per_share = Column(DECIMAL(20, 8), comment="WIND-每股红利股")
    tx_register_date = Column(Date, comment="天相-登记日")
    tx_except_date = Column(Date, comment="天相-除权日")
    tx_receipt_date = Column(Date, comment="天相-到账日")
    tx_cash_per_share = Column(DECIMAL(20, 8), comment="天相-每股派现金")
    tx_bonus_per_share = Column(DECIMAL(20, 8), comment="天相-每股红利股")
    jc_register_date = Column(Date, comment="巨潮-登记日")
    jc_except_date = Column(Date, comment="巨潮-除权日")
    jc_receipt_date = Column(Date, comment="巨潮-到账日")
    jc_cash_per_share = Column(DECIMAL(20, 8), comment="巨潮-每股派现金")
    jc_bonus_per_share = Column(DECIMAL(20, 8), comment="巨潮-每股红利股")
    create_time = Column(DateTime, comment="创建时间", server_default=func.now(), index=True)
    UniqueConstraint(biz_date, board, market, stk_code, right_type)


class BaseTable(Base):
    __abstract__ = True  # 加了该属性后生成表的时候不会生成该表
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    # create_user =  Column( Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)
    # update_user =  Column( Integer, default=user_service.get_id_by_token, onupdate=user_service.get_id_by_token)


class EnumConfig(BaseTable):
    """
    # 状态迁移--临时计算,唯一字段, eg:用户状态,系统状态,目标状态

    用户修改枚举表,
    用户配置表
    系统枚举,配置表

    校验用户权限

    场景:

        1. 枚举,常量 (系统,用户配置) ,,
        2. 下拉菜单,类似list
        3. 省市区级联下拉菜单

    树形结构????
    二维结构,目录与文件同级?? 深圳市,广东省, 市级, 直辖市, 人口????
    """
    __tablename__ = 'enum_config'
    code = Column(String(255), unique=True, comment="枚举key值")  # code唯一 or 联合唯一?? 用户code随机生成
    value = Column(String(255), comment="枚举value数据")
    # value: shenzhen,code:shenzhen_city,
    group_code = Column(String(255), unique=True, comment="分组code")  # group_code也有树形结构?,唯一
    parent_id = Column(Integer, Sequence('sort_seq'), comment="父级id", server_default='0')

    comment = Column(String(255), comment="备注")
    # cfg_value_type=Column(String(255)) 配置值类型，比如integer（整数）、html（HTML）等bool（是否），不同的值类型可以通过不同的表单来显示和编辑
    sort = Column(Integer, comment="排序字段")
    create_by = Column(String(255), server_default='SYSTEM', comment="创建者")


if __name__ == '__main__':
    sqlserver_url = 'mysql+pymysql://{}:{}@{}/{}'.format('root', "123456", "127.0.0.1", 'test')
    engine = create_engine(sqlserver_url, echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
