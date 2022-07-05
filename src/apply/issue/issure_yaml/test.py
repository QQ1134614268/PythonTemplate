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
        pass
