from apply.issue.issue_api.models import AuthMenu
from conf.config import dev_test_session, pro_test_session
from util.cache_util import list_to_file


@list_to_file("dev.out.txt")
def get_db():
    vos = shenwan_auth_session.query(AuthMenu).all()
    ret = []
    for vo in vos:
        ret.append(f'{vo.name}-{vo.item_en_name}')
    ret.sort()
    return ret


@list_to_file("uat.out.txt")
def get_uat_db():
    vos = dev_test_session.query(AuthMenu).all()
    ret = []
    for vo in vos:
        ret.append(f'{vo.name}-{vo.item_en_name}')
    ret.sort()
    return ret


@list_to_file("pro.out.txt")
def get_pro_db():
    vos = pro_test_session.query(AuthMenu).all()
    ret = []
    for vo in vos:
        ret.append(f'{vo.name}-{vo.item_en_name}')
    ret.sort()
    return ret


if __name__ == '__main__':
    # get_uat_db()
    # get_db()
    get_pro_db()