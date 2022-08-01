import json
from unittest import TestCase

from sqlalchemy import Column, MetaData, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import declarative_base

from conf.config import localhost_oa_session

metadata = MetaData()

Base = declarative_base()


class Menu(Base):
    __tablename__ = 'menu'
    # __bind_key__ = 'oa'  # flask_sqlalchemy中生效

    # __table_args__ = {   # sqlalchemy中生效
    #     'schema': 'oa'
    # }
    id = Column(INTEGER, primary_key=True, )
    menuName = Column("menu_name", String(64))
    parentId = Column("parent_id", INTEGER)
    isSelect = Column("is_Select", String)
    menuOrder = Column("menu_Order", INTEGER)


class TestAutoCode(TestCase):
    def test_run(self):
        with open("xx.json", encoding="utf-8", mode='r') as f:
            menu_list = json.loads(f.read())

        self.insert_menu(menu_list, None)

    def insert_menu(self, menu_list, parent_id):
        if not menu_list:
            return
        for index, menu_dic in enumerate(menu_list):
            vo = Menu(
                menuName=menu_dic.get("name").replace("\n", "").replace(" ", ""),
                parentId=parent_id,
                isSelect=True,
                menuOrder=index
            )
            localhost_oa_session.add(vo)
            localhost_oa_session.commit()
            self.insert_menu(menu_dic.get("children"), vo.id)

    def test_run2(self):
        localhost_oa_session.query(Menu).delete()
        with open("menu.json", encoding="utf-8", mode='r') as f:
            menu_list = json.loads(f.read())

        self.insert_menu2(menu_list)

    def insert_menu2(self, menu_list):
        if not menu_list:
            return
        for index, menu_dic in enumerate(menu_list):
            vo = Menu(
                id=menu_dic.get("id"),
                menuName=menu_dic.get("label"),
                parentId=menu_dic.get("pid"),
                isSelect=True,
                menuOrder=index
            )
            localhost_oa_session.add(vo)
            localhost_oa_session.commit()
            self.insert_menu2(menu_dic.get("children"))
