# -*- coding:utf-8 -*-
"""
@Time: 2021/12/29
@Description:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from apply.issue.issue_api.models import AuthMenu
from conf.sw_config import sqlserver_url

text = """UPDATE auth.auth_menu SET serial_no=2 WHERE id=17;
UPDATE auth.auth_menu SET serial_no=3 WHERE id=20;
UPDATE auth.auth_menu SET serial_no=4 WHERE id=1;
UPDATE auth.auth_menu SET serial_no=5 WHERE id=24;
UPDATE auth.auth_menu SET serial_no=6 WHERE id=28;
UPDATE auth.auth_menu SET serial_no=7 WHERE id=46;
UPDATE auth.auth_menu SET serial_no=1 WHERE id=18;
UPDATE auth.auth_menu SET serial_no=2 WHERE id=19;
UPDATE auth.auth_menu SET serial_no=4 WHERE id=40;
UPDATE auth.auth_menu SET serial_no=3 WHERE id=42;
UPDATE auth.auth_menu SET serial_no=5 WHERE id=44;
UPDATE auth.auth_menu SET serial_no=6 WHERE id=45;
UPDATE auth.auth_menu SET serial_no=1 WHERE id=21;
UPDATE auth.auth_menu SET serial_no=2 WHERE id=22;
UPDATE auth.auth_menu SET serial_no=6 WHERE id=23;
UPDATE auth.auth_menu SET serial_no=7 WHERE id=39;
UPDATE auth.auth_menu SET serial_no=4 WHERE id=52;
UPDATE auth.auth_menu SET serial_no=3 WHERE id=53;
UPDATE auth.auth_menu SET serial_no=5 WHERE id=54;
UPDATE auth.auth_menu SET serial_no=9 WHERE id=61;
UPDATE auth.auth_menu SET serial_no=8 WHERE id=68;
UPDATE auth.auth_menu SET serial_no=2 WHERE id=3;
UPDATE auth.auth_menu SET serial_no=3 WHERE id=4;
UPDATE auth.auth_menu SET serial_no=1 WHERE id=16;
UPDATE auth.auth_menu SET serial_no=4 WHERE id=38;
UPDATE auth.auth_menu SET serial_no=6 WHERE id=41;
UPDATE auth.auth_menu SET serial_no=5 WHERE id=60;
UPDATE auth.auth_menu SET serial_no=1 WHERE id=25;
UPDATE auth.auth_menu SET serial_no=2 WHERE id=26;
UPDATE auth.auth_menu SET serial_no=3 WHERE id=27;
UPDATE auth.auth_menu SET serial_no=1 WHERE id=29;
UPDATE auth.auth_menu SET serial_no=2 WHERE id=30;
UPDATE auth.auth_menu SET serial_no=3 WHERE id=31;
UPDATE auth.auth_menu SET serial_no=1 WHERE id=47;
 
UPDATE auth.auth_menu SET parent_id=NULL,name='舆情首页',serial_no=9 WHERE id=56;
 
UPDATE auth.auth_menu SET name='股票质押舆情',serial_no=10 WHERE id=55;
 
UPDATE auth.auth_menu SET name='质押标的评分',serial_no=2 WHERE id=57;
UPDATE auth.auth_menu SET name='融资人舆情',serial_no=4 WHERE id=62;
UPDATE auth.auth_menu SET name='标的券舆情',serial_no=3 WHERE id=58;
UPDATE auth.auth_menu SET name='证券风险分析',serial_no=1 WHERE id=59;
 
UPDATE auth.auth_menu SET name='系统管理',serial_no=11 WHERE id=65;
 
 
UPDATE auth.auth_menu SET serial_no=1,parent_id=65 WHERE id=50;
UPDATE auth.auth_menu SET parent_id=65,serial_no=2 WHERE id=51;
UPDATE auth.auth_menu SET name='方案配置',serial_no=4 WHERE id=64;
UPDATE auth.auth_menu SET serial_no=5 WHERE id=66;
UPDATE auth.auth_menu SET serial_no=6 WHERE id=67;
UPDATE auth.auth_menu SET name='分组管理',parent_id=65,serial_no=3 WHERE id=63;
UPDATE auth.auth_menu SET serial_no=2 WHERE id=5;
UPDATE auth.auth_menu SET serial_no=1 WHERE id=6;
UPDATE auth.auth_menu SET serial_no=3 WHERE id=7;
UPDATE auth.auth_menu SET serial_no=4 WHERE id=43;
UPDATE auth.auth_menu SET serial_no=12 WHERE id=2;
UPDATE auth.auth_menu SET serial_no=1 WHERE id=69;
"""


# UPDATE auth.auth_menu SET name='质押业务分析',serial_no=8 WHERE id=49;
# 49 company_risk


def main():
    engine = create_engine(sqlserver_url, echo=True)
    session = sessionmaker(bind=engine)()
    lines = text.split("\n")
    ret = []
    try:
        for line in lines:
            line = line.strip()
            if line:
                arr = line.rsplit("=", 1)

                name = session.query(AuthMenu.item_en_name).filter(AuthMenu.id == arr[1].replace(";", "")).scalar()
                line = arr[0] + "='" + name + "';\n"
                assert len(line.split(" id=")) == 2, "Exception"
                line = line.replace(" id=", " item_en_name=")
                ret.append(line)
    except:
        print(line)
    with open("a.txt", encoding="utf-8", mode='w') as f:
        f.writelines(ret)


if __name__ == '__main__':
    main()
