# -*- coding:utf-8 -*-
"""
@Time: 2021/11/19
@Description:
"""


def get_tree_merge(data_list, row=1, col=1):
    res = []
    if not data_list:
        return res
    for index, val in enumerate(data_list):
        res.extend(_get_merge_cells(val, row + index, col))
        get_tree_merge(val.get("children"), row + index, col + len(val) - 1)
    return res


def _get_merge_cells(val, row=1, col=1):
    ret = []
    if isinstance(val.get("children"), list) and len(val.get("children")):
        for i in range(len(val.keys()) - 1):
            ret.append({
                "start_row": row,
                'start_column': col + i,
                'end_row': row + len(val.get("children")) - 1,
                'end_column': col + i
            })
    return ret


def get_style():
    # 上下居中, 靠左
    pass


def write_to_excel():
    pass
