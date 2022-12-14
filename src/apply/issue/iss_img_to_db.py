# -*- coding:utf-8 -*-
"""
@Time: 2022/10/19
@Description: todo img脚本,优化--mapreduce env, filter
"""
import os
import os.path
from os import listdir
from os.path import abspath, join
from unittest import TestCase

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_session
from config.model import BaseTable

Base = declarative_base()


class Img(BaseTable):
    __tablename__ = 'img'
    __table_args__ = {
        'schema': 'jiangxin'
    }
    name = Column(String(64))
    description = Column(String(64))
    img = Column(String(64))
    parent_id = Column(Integer)
    type_id = Column(Integer)


# 递归遍历目录
def traversal_files(path):
    for dir1 in os.listdir(path):
        dir1 = os.path.join(path, dir1)
        print(dir1)
        # 判断当前目录是否为文件夹
        if os.path.isdir(dir1):
            traversal_files(dir1)


class TestAutoCode(TestCase):

    def test_run(self):
        env = {
            "root_path": ".",
            "level": 1,
            "type_dir": "",
            "dirs": {
                "home": "",
                "type": "",
                "content": ""
            }
        }
        path = r"E:\workspace\JavaSpace\TemplateBoot\JiangXin\web\src\assets\renderings_imgs"
        # 分类目录
        type_dirs = []
        for dir1 in os.listdir(path):
            dir1 = os.path.join(path, dir1)
            if os.path.isdir(dir1):
                type_dirs.append(dir1)
        #
        art_dirs = []
        for dir1 in type_dirs:
            for file in os.listdir(dir1):
                full_file = os.path.join(dir1, file)
                art_dirs.append(full_file)

        for dir1 in art_dirs:
            home = ""
            for index, img in enumerate(os.listdir(dir1)):
                if index == 0:
                    home = Img(name=dir1[dir1.rindex("\\") + 1:], description=img, type_id=1, parent_id=0, img=img)
                    localhost_test_session.add(home)
                    localhost_test_session.commit()
                else:
                    vo = Img(name="", description=img, type_id=1, parent_id=home.id, img=img)
                    localhost_test_session.add(vo)
                    localhost_test_session.commit()

        # # 迁移文件
        # imgs = []
        # out_dir = ""
        # for dir1 in art_dirs:
        #     for dir2 in os.listdir(dir1):
        #         dir2 = os.path.join(dir1, dir2)
        #         imgs.append(dir2)
        #         copyfile(dir2, out_dir)


def show(path):
    for item in listdir(path):
        print(os.path.abspath(path))
        if '.idea' == item:
            continue
        if os.path.isfile(item):
            continue
        item = abspath(join(path, item))
        print(item)
        for sub in listdir(item):
            sub = join(item, sub)
            print(sub)
            show(sub)


if __name__ == '__main__':
    print(os.path.abspath('.'))
