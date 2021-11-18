# -*- coding:utf-8 -*-
"""
@Time: 2021/11/18
@Description:
"""
import json
from copy import deepcopy

from openpyxl import Workbook


def test1():
    with open("ds_1.json", encoding="utf-8") as f:
        con = f.read()
        data = json.loads(con)
        data_list = data["data"]['totalList']
        for model in data_list:
            ret = {
                "name": "",
                "desc": "",
            }
            ret["name"] = model["name"]
            ret["desc"] = model["description"]


# @file_cache("tree_data.json")
def test_2():
    ret = []
    with open("ds_2.json", encoding="utf-8") as f:

        data = json.loads(f.read())
        job_list = data["data"]

        for job in job_list:
            job_data = {'job_name': job['name'], 'job_desc': job['description'], 'children': [], }
            step_dic = json.loads(job['processDefinitionJson'])
            for step in step_dic["tasks"]:
                task_data = {
                    'task_name': step["name"],
                    'task_desc': step["description"],
                    'task_type': step["type"],
                    'task_script': step.get('params', {}).get('rawScript')
                }
                job_data['children'].append(task_data)
            ret.append(job_data)
    return ret


data = [{"ren": "ren1", 'name': [{"en_name": 1, "cn_name": 2}]},
        {"ren": "ren2", 'name': [{"en_name": 1, "cn_name": 2}]},
        {"ren": "ren3", 'name': [{"en_name": 1, "cn_name": 2}]}]


# @file_cache("list_data.json")
def two2one_step1(data_list):
    res = []
    for model in data_list:
        if isinstance(model.get("children"), list):
            c_list = model.pop("children")
            res = two2one2(model, c_list)
            return two2one_step1(res)
    return res


def tet(data_list):
    ret = []
    for item in data_list:
        if isinstance(item.get("children"), list) and item.get("children"):
            ret.extend(tet(trans(item)))
        else:
            ret.append(item)
    return ret


def trans(dic):
    ret = []
    for item in dic.pop("children"):
        new = deepcopy(dic)
        new.update(item)
        ret.append(new)
    return ret


def two2one2(p_dic, c_list):
    if not (p_dic and c_list):
        return c_list

    if list(set(list(p_dic.keys())) & set(c_list[0].keys())):
        assert "命名重复", list(set(list(p_dic.keys())) & set(c_list[0].keys()))

    ret = []
    for model in c_list:
        new = deepcopy(p_dic)
        new.update(model)
        ret.append(new)
    return ret


# @file_cache("merge_data.json")
def get_merge(data_list, row=0, col=0):
    res = []
    for val in data_list:
        if isinstance(val.get("children"), list):
            c_list = val.pop("children")
            res.append(two2onemearge(val, c_list, col, ))
            get_merge(c_list, row + len(val.keys()), col + len(c_list))
    return res


def two2onemearge(p_dic, data_list, row, col=0):
    row_end = row + len(p_dic.keys())
    ret = []
    for i in range(row, row_end):
        ret.append((row, row_end, col, col + len(data_list)))
    return ret


def write():
    tree_data = test_2()
    list_data = tet(deepcopy(tree_data))
    merge_data = get_merge(tree_data)
    import time
    wb = Workbook()
    sheet = wb.active
    for data in list_data:
        sheet.append(list(data.values()))
    wb.save("sample{}.xlsx".format(time.time()))


if __name__ == '__main__':
    write()
