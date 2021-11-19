# -*- coding:utf-8 -*-
"""
@Time: 2021/11/19
@Description:
"""
from copy import deepcopy


def tree_to_list(data_list):
    ret = []
    for item in data_list:
        if item.get("children") and isinstance(item.get("children"), list):
            ret.extend(tree_to_list(_release_children(item)))
        else:
            return data_list
    return ret


def _release_children(dic):
    child = dic.pop("children")
    # child = dic.get("children")
    if child:
        repeat = set(dic) & (set(child[0]))
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
