# coding:utf-8
import logging


def create_log(filename='D:/bat/log/task3.log'):
    formatter_str = '[%(asctime)s][%(filename)s] -- %(message)s'  # 日志格式
    formatter = logging.Formatter(formatter_str)
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(filename)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)  # 添加标准输出
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == '__main__':
    log = create_log()
    log.info("你好")
