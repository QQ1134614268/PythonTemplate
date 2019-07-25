# -*- coding: utf-8 -*-
"""
# @Time    : 2019/7/24 13:52
# @Author  : huangran
"""
# 增
# 改
# 查
# 删


def getUserById(userId):
    # 查
    pass


def getUserAll():
    pass


def getUserByArea(area):
    pass


# def getUserByConditions(area, userType):
#     pass
#
#
# def getPageUserByConditions(area, userType, limit, page):
#     pass


def getPageUserByConditions(area, userType, limit, page, is_page=False):
    # 分页 多条件筛选
    # return数据库数据,前端组合展示, -- 开始时间 平均年龄 -- 计算所得
    # count基数
    query = {"area": area, "userType": userType}
    page_help(query, limit, page)
    pass


def getUserByConditionsToCsv(area, userType):
    #  多条件筛选  所见即所得
    getPageUserByConditions(area, userType, is_page=False)
    pass


def page_help(area, userType, limit, page):
    # todo sort排序
    # 返回 list count
    pass
