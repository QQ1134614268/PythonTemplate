# -*- coding:utf-8 -*-
"""
@Time: 2022/8/11
@Description:
"""
from os import path

from conf.config import DATA_DIR


def get_data_dir(file_path):
    return path.join(DATA_DIR, file_path)
