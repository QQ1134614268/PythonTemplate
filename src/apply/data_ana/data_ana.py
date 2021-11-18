# -*- coding:utf-8 -*-
"""
@Time: 2021/11/18
@Description:
"""
import json
from copy import deepcopy


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


def test_2():
    with open("ds_2.json", encoding="utf-8") as f:
        data = json.loads(f.read())
        job_list = data["data"]
        for job in job_list:
            step_dic = json.loads(job['processDefinitionJson'])

            for step in step_dic["tasks"]:
                task_name = step["name"]
                task_desc = step["description"]
                task_type = step["type"]
                task_script = step['params']["rawScript"]


data = [{"ren": "ren1", 'name': [{"en_name": 1, "cn_name": 2}]},
        {"ren": "ren2", 'name': [{"en_name": 1, "cn_name": 2}]},
        {"ren": "ren3", 'name': [{"en_name": 1, "cn_name": 2}]}]


def two2one_step1(data_list):
    for model in data_list:
        for key, val in model.items():
            if isinstance(val.get("children"), list):
                c_list = val.pop("children")
                res = two2one2(val, c_list)
                return two2one_step1(res)


def two2one2(p_dic, c_list):
    if not p_dic or c_list:
        return c_list

    if list(set(list(p_dic.keys())) & set(c_list[0].keys())):
        assert "命名重复", list(set(list(p_dic.keys())) & set(c_list[0].keys()))

    ret = []
    for model in c_list:
        new = deepcopy(p_dic)
        new.update(model)
        ret.append(new)
    return ret


def get_merge(data_list, row, col=0):
    res = []
    for model in data_list:
        for key, val in model.items():
            if isinstance(val.get("children"), list):
                c_list = val.pop("children")
                res = two2onemearge(val, c_list, col, )
                res.append(get_merge(res, row + len(val.keys()), col + len(c_list)))

    return res


def two2onemearge(p_dic, data_list, row, col=0):
    row_end = row + len(p_dic.keys())
    ret = []
    for i in range(row, row_end):
        ret.append((row, row_end, col, col + len(data_list)))
    return ret


if __name__ == '__main__':
    test1()
    test_2()
