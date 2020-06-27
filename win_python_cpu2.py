# -*- coding:utf-8 -*-
import logging
import time

import psutil
from util import file_util


def create_logger_t2(file_path='F:/log/log.log'):
    file_path = file_util.prepare_file(file_path)

    formatter_str = '[%(asctime)s][%(filename)s] -- %(message)s'  # 日志格式
    # formatter_str = '{"time":"%(asctime)s","levelname":"%(levelname)s","path":"%(filename)s %(lineno)d","message":%(message)s,"type":"log"}'
    formatter = logging.Formatter(formatter_str)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(file_path)
    # rHandler = ConcurrentRotatingFileHandler(file_path, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf_8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)  # 添加标准输出

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def cpu():
    log = create_logger_t2()
    while True:
        time.sleep(1)
        cpu_liyonglv = psutil.cpu_percent()
        log.info("当前cpu利用率：\033[1;31;42m%s%%\033[0m" % cpu_liyonglv)


if __name__ == '__main__':
    cpu()
