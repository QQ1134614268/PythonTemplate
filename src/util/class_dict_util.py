import decimal
import uuid
from datetime import datetime, date
from enum import Enum

from config.time_conf import DATE_TIME_FORMAT, DATE_FORMAT


def class_to_dict(obj):
    """
    把对象(支持单个对象、list、set)转换成字典
    """
    is_list = obj.__class__ == [].__class__  # 内部的数据是不是列表,也就是可迭代对象
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            obj_arr.append(class_to_dict(o))
        return obj_arr
    if hasattr(obj, '__dict__'):  # 开始走这里
        dic = {}
        for key, value in obj.__dict__.items():
            dic[key] = class_to_dict(value)  # 开始走递归,也就是为了取他内部的所有数据,只要内部有可迭代的数据,就会一直调用.
        return dic

    if isinstance(obj, datetime):
        return obj.strftime(DATE_TIME_FORMAT)
    if isinstance(obj, date):
        return obj.strftime(DATE_FORMAT)
    if isinstance(obj, (decimal.Decimal, uuid.UUID)):
        return str(obj)
    if isinstance(obj, Enum):
        return obj.name
    return obj


def class_from_dict(cls, kwargs):
    """
 　　cls : 类名称
 　　kwargs: 类参数
 　　"""
    return cls(**kwargs)
