# -*- coding:utf-8 -*-
"""
@Time: 2021/11/19
@Description:
"""
from copy import deepcopy


def tree_to_list(data_list):
    ret = []
    if not data_list:
        return ret

    for item in data_list:
        ret.extend(tree_to_list(_release_children(item)))
    return ret


def _release_children(dic):
    assert isinstance(dic.get("children"), list), "数据格式错误,缺少children字段"
    child = dic.pop("children")
    # child = dic.get("children")
    if child:
        repeat = set(dic).union(set(child[0]))
        assert not repeat, "命名重复".format(repeat)
        ret = []
        for item in child:
            new = deepcopy(dic)
            new.update(item)
            ret.append(new)
        dic["children"] = child  # 恢复
        return ret

    ret = [deepcopy(dic)]
    dic["children"] = child  # 恢复
    return ret
