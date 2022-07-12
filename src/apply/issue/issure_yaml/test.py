import json
from unittest import TestCase

from apply.issue.issure_db_excel.models import MysqlTables
from conf.config import localhost_oa_session


#  todo  yaml tree json arr 工具类
class AutoInt:
    pass


class TestAutoCode(TestCase):
    def test_to_prop(self):
        vos = localhost_oa_session.query(MysqlTables).filter(
            MysqlTables.TABLE_SCHEMA == "oa"
        ).all()
        vos.sort(key=lambda x: x.TABLE_COMMENT)
        lines = [vo.TABLE_COMMENT for vo in vos]
        new_lines = []
        for line in lines:
            line = line.replace("/", ".")
            if "." in line:
                index = line.rfind(".")
                line = line[0:index] + "=" + line[index + 1:]
            # line = line.f("/", "=", 1)
            new_lines.append(line)

    def test_to_yaml(self):
        vos = localhost_oa_session.query(MysqlTables).filter(
            MysqlTables.TABLE_SCHEMA == "oa"
        ).all()
        vos.sort(key=lambda x: x.TABLE_COMMENT)
        root = {}
        parent = {}
        for vo in vos:
            arr = vo.TABLE_COMMENT.split("/")
            for name in arr:
                index = arr.index(name)
                node = {
                    "level": index,
                    "name": name,
                    "child": []
                }
                if name not in parent:
                    parent[name] = node
                if index == 0 and name not in root:
                    root[name] = node
                if index != 0:
                    parent[arr[index - 1]]["child"].append(node)
        res = []
        self.dic_to_yaml(root.values(), res)
        with open("xx.yaml", "w+", encoding="utf-8") as f:
            f.write("\n".join(res))

    def dic_to_yaml(self, arr, res):
        if not arr:
            return
        for item in arr:
            res.append(item["level"] * "  " + item["name"])
            self.dic_to_yaml(item["child"], res)

    def test_yaml_to_db(self):
        with open("xx.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        tree = []
        for i in range(len(lines)):
            line = lines[i]
            dic = {
                "name": line,
                "db_line": line.lstrip(),
                "children": []
            }
            self.get_child(dic, lines[i + 1:])
            if line.lstrip() == line:
                tree.append(dic)
        with open("xx.json", "w+", encoding="utf-8") as f:
            f.write(json.dumps(tree, ensure_ascii=False))

    def get_child(self, dic, lines, step=2):
        if not lines:
            return
        line = dic["name"]
        ret = dic["children"]
        for i in range(len(lines)):
            child_line = lines[i]
            if self.get_level2(line, child_line) < step:
                return
            if self.get_level2(line, child_line) > step:
                continue
            if self.get_level2(line, child_line) == step:
                dic2 = {
                    "name": child_line,
                    "db_line": child_line.lstrip(),
                    "children": []
                }
                ret.append(dic2)
                self.get_child(dic2, lines[i:])

    def get_level(self, line):
        return len(line) - len(line.lstrip())

    def get_level2(self, p_line, c_line):
        return self.get_level(c_line) - self.get_level(p_line)
