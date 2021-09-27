# -*- coding:utf-8 -*-
"""
@Time: 2021/7/30
@Description:
"""
import re

with open("dongcai_data.txt", encoding="utf-8") as f:
    lines = f.readlines()
ret = []
mo = {}
for index, line in enumerate(lines):
    line = line.replace("\n", "")
    if "# 数据说明" == line:
        arr = lines[index + 1].split("--")
        if mo:
            ret.append(mo)
        mo = {
            "title": arr[0].replace(" ", ""),
            "table": re.sub("[\u4e00-\u9fa5\,\。]", "", arr[1].replace("\n", "").replace(" ", "")),
        }

    if line.startswith("Topic:"):
        mo["topic"] = line.split(":")[1].replace("\n", "").replace(" ", "")
    if line.startswith("key:"):
        mo["key"] = line.split(":")[1].replace("\n", "").replace(" ", "")
    if '":' in line:
        arr = line.split('":')
        code = arr[0].replace('"', "").replace(" ", "").replace("{", "")
        mo.setdefault("field", [])
        mo["field"].append(code)
else:
    if mo:
        ret.append(mo)

template = """
    {{
        "title": "{title}",
        "topic": "{topic}",
        "key": "{key}",
        "table": "{table}",
        "valueType": "array",
        "fields": [{Field}]
    }}
"""
res = []
for item in ret:
    tmp = []
    for val in item["field"]:
        tmp.append("""{{"jsonField": "{}", "dbField": "{}", "emptyToNull": "true"}}""".format(val, val))
    item["Field"] = ",".join(tmp)
    res.append(template.format(**item))
    # print(template.format(**item))
# print("[{}]".format(",".join(res)))
with open("dongcai_result.py", mode="w", encoding="utf-8") as f:
    f.write("[{}]".format(",".join(res)))
