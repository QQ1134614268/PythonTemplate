# -*- coding:utf-8 -*-
"""
@Time: 2021/10/9
@Description:
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description='一个示例命令行工具，接受已知和未知的选项参数')
    parser.add_argument('integers', metavar='1', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parser.add_argument('-x', nargs=2)
    parser.add_argument('--version', '-v', help='verbose mode')
    parser.add_argument('--mode', '-m', help='verbose mode')
    parser.add_argument('--config', '-c', help='配置文件位置')
    # 定义一个已知的选项参数
    # 添加--verbose标签，标签别名可以为-v，这里action的意思是当读取的参数中出现--verbose/-v的时候
    # 参数字典的verbose建对应的值为True，而help参数用于描述--verbose参数的用途或意义。
    parser.add_argument('--verbose', action='store_true', help='增加输出信息')
    # 解析已知的命令行参数，并收集未知的参数
    args = parser.parse_args()  # 命令行中出现未定义参数会退出
    known_args, unknown_args = parser.parse_known_args()

    # 输出已知的选项参数
    if known_args.verbose:
        print('Verbose mode is on.')

        # 输出未知的参数
    print('接收到的未知参数:')
    for arg in unknown_args:
        print(arg)


if __name__ == "__main__":
    main()
