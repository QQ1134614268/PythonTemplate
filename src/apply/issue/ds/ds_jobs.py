# -*- coding:utf-8 -*-
"""
@Time: 2021/11/18
@Description:
"""
import json

import time
from openpyxl import Workbook

from util.tree_util import tree_to_list


def decode_file():
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


def write_to_excel():
    tree_data = decode_file()
    list_data = tree_to_list(tree_data)
    wb = Workbook()
    sheet = wb.active
    for data in list_data:
        sheet.append(list(data.values()))

    # merge_data = get_merge(tree_data)
    # for merge_cell in merge_data:
    #     sheet.merge_cells(**merge_cell)

    wb.save("sample{}.xlsx".format(time.time()))  # save会调用close


if __name__ == '__main__':
    write_to_excel()
