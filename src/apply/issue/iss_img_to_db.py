# -*- coding:utf-8 -*-
"""
@Time: 2022/10/19
@Description: todo img脚本,优化--mapreduce env, filter
"""
import os
import os.path
from datetime import datetime
from os import listdir
from os.path import abspath, join
from unittest import TestCase

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_session

Base = declarative_base()


class Img(Base):
    __tablename__ = 'img'
    __table_args__ = {
        'schema': 'jiangxin'
    }
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")

    name = Column(String(64))
    description = Column(String(64))
    imgUrl = Column(String(64))
    parent_id = Column(Integer)
    type_id = Column(Integer)

    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, comment="修改时间")
    create_by = Column(Integer, default="-1", comment="创建者id")
    update_by = Column(Integer, default="-1", comment="修改者id")


# 递归遍历目录
def traversal_files(path):
    for dir1 in os.listdir(path):
        dir1 = os.path.join(path, dir1)
        print(dir1)
        # 判断当前目录是否为文件夹
        if os.path.isdir(dir1):
            traversal_files(dir1)


class TestImgToDB(TestCase):

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
                    home = Img(name=dir1[dir1.rindex("\\") + 1:], description=img, type_id=1, parent_id=0, imgUrl=img)
                    localhost_test_session.add(home)
                    localhost_test_session.commit()
                else:
                    vo = Img(name="", description=img, type_id=1, parent_id=home.id, imgUrl=img)
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
