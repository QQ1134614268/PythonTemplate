import execjs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from apply.issue.issue_api.models import AuthMenu
from conf.sw_config import SHENWAN_AUTH_URL
from util.cache_util import list_to_file


def get_menu_list():
    with open('test_input.js', encoding='utf-8') as f:
        doc_js = execjs.compile(f.read())
    # python.exe -X utf8 s2.py
    # 不能有 export

    # 调用函数
    # res = doc_js.call('createGuid')
    return doc_js.eval('menu_list')


@list_to_file("db.out.txt")
def get_db():
    engine = create_engine(SHENWAN_AUTH_URL, echo=True)
    session = sessionmaker(bind=engine)()
    vos = session.query(AuthMenu).all()
    ret = []
    for vo in vos:
        ret.append(f'{vo.name}-{vo.item_en_name}')
    ret.sort()
    return ret


def get_from(menu_list):
    ret = []
    for dic in menu_list:

        ret.append(f'{dic["title"]}-{dic["id"]}')
        if dic.get('children'):
            ret.extend(get_from(dic.get('children')))
    return ret


@list_to_file('js.out.txt')
def get_res(menu_list):
    ret = get_from(menu_list)
    ret.sort()
    return ret


if __name__ == '__main__':
    menu_children = get_menu_list()
    # menu_list_file = get_from(menu_children)
    get_res(menu_children)
    get_db()
    # from collections import Counter
    #
    # b = dict(Counter(menu_list_file))
    # print([key for key, value in b.items() if value > 1])  # 只展示重复元素
    #
    # menu_list_file_set = set(menu_list_file)
    # menu_list_db = get_db()
    # menu_list_db_set = set(menu_list_db)
    #
    # c1 = menu_list_file_set - menu_list_db_set
    # c12 = menu_list_db_set - menu_list_file_set
    # print(len(menu_list_file), len(menu_list_file_set), len(menu_list_db), len(menu_list_db_set), )
    # print(c1 == c12, c1, c12)
