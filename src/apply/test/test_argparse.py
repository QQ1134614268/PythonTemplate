# -*- coding:utf-8 -*-
"""
@Time: 2021/10/9
@Description:
"""
import argparse

parser = argparse.ArgumentParser(prog='PROG', description='Process some integers.')
parser.add_argument('integers', metavar='1', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('-x', nargs=2)
parser.add_argument('--version', '-v', help='verbose mode')
parser.add_argument('--mode', '-m', help='verbose mode')
# 添加--verbose标签，标签别名可以为-v，这里action的意思是当读取的参数中出现--verbose/-v的时候
# 参数字典的verbose建对应的值为True，而help参数用于描述--verbose参数的用途或意义。
args = parser.parse_args()  # 将变量以标签-值的字典形式存入args字典
print(args)
print(args.mode)
