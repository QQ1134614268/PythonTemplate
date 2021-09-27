# -*- coding:utf-8 -*-
"""
@Time: 2021/7/30
@Description:
"""
from src.util.log_util import logger

with open("excel_field_data.txt", encoding="utf-8") as f:
    lines = f.readlines()
ret = []
template = """    @ExcelProperty(index = {}, value = "{}")
    private String {};\n"""
for index, line in enumerate(lines):
    if "###" in line:
        print("-------------")
        new = index
        continue
    line = line.replace("\n", "").strip()
    arr = line.split("\t")
    arr = [i for i in arr if i.strip()]
    if len(arr) == 2:
        ret.append({
            "index": index - new-1,
            "value": arr[0],
            "name": arr[1],
        })
    else:
        logger.error(arr)
with open("excel_field_output.txt", mode="w", encoding="utf-8") as f:
    for j in ret:
        f.write(template.format(j["index"], j["value"], j["name"], ))
