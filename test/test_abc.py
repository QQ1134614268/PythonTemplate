# -*- coding:utf-8 -*-
"""
@Time: 2021/8/10
@Description:
"""
import abc


class CashAndStock(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_stock_0(self):
        pass


class Child(CashAndStock):
    def get_stock_0(self):
        return 1


if __name__ == '__main__':
    Child().get_stock_0()
