import os
from unittest import TestCase

import jinja2

from apply.issue.issure_js_auto_code.config import localhost_oa_engine
from apply.issue.issure_js_auto_code.util import res_to_dict
from util.str_util import to_lower_camel, to_snake, to_upper_camel


class Form:

    @staticmethod
    def get_tables(db):
        sql = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = %(db)s"
        res = localhost_oa_engine.execute(sql, {"db": db})
        return res_to_dict(res)

    @staticmethod
    def get_table_info(table_name, db=None):
        # 表名,表注释
        # 字段名,字段类型,字段注释, 枚举值

        # json数据 -- class数据-- 类数据
        sql = """SELECT COL.COLUMN_NAME, COL.COLUMN_TYPE, COL.COLUMN_COMMENT, COL.DATA_TYPE 
        FROM INFORMATION_SCHEMA.COLUMNS COL 
        Where COL.table_schema = %(db)s AND COL.TABLE_NAME = %(table_name)s"""

        args = {"db": db, "table_name": table_name}
        res = localhost_oa_engine.execute(sql, args)
        data = res_to_dict(res)
        for item in data:
            item["COLUMN_NAME"] = to_lower_camel(item["COLUMN_NAME"])
        return data

    @staticmethod
    def to_file(data_dic, path, resource_dir, template_file):
        template_loader = jinja2.FileSystemLoader(searchpath=resource_dir)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(template_file)
        output_text = template.render(data_dic)
        with open(path, "w", encoding="utf-8") as f:
            f.write(output_text)


class TestAutoCode(TestCase):

    def test_run(self):
        table = "organization"
        rows = Form.get_table_info(table, "oa")
        data = {
            "list": rows
        }
        Form.to_file(data, f"{table}.vue".format(table), os.path.dirname(__file__), "templates/vue.template")

    def test_run_all(self):
        tables = Form.get_tables("oa")
        for table in tables:
            table_name = table["TABLE_NAME"]
            table_upper_caml = to_upper_camel(table_name)
            rows = Form.get_table_info(table_name, "oa")
            data = {
                "list": rows,
                "tableUpperCaml": table_upper_caml,
                "tableConst": to_snake(table_name).upper(),
            }
            Form.to_file(data, f"tmp/{table_upper_caml}.vue", os.path.dirname(__file__), "templates/vue.template")

    def test_run_index_js(self):
        tables = Form.get_tables("oa")
        table_infos = []
        for table in tables:
            table_name = table["TABLE_NAME"]
            table_upper_caml = to_upper_camel(table_name)
            table_infos.append({
                "tableUpperCaml": table_upper_caml,
                "tableLowerCaml": to_lower_camel(table_name),
                "tableConst": to_snake(table_name).upper(),
            })
        data = {
            "list": table_infos
        }
        Form.to_file(data, "tmp/routes.js", "templates/routes.template")

    def test_run_config_js(self):
        tables = Form.get_tables("oa")
        table_infos = []
        for table in tables:
            table_name = table["TABLE_NAME"]
            table_upper_caml = to_upper_camel(table_name)
            table_infos.append({
                "tableUpperCaml": table_upper_caml,
                "tableLowerCaml": to_lower_camel(table_name),
                "tableConst": to_snake(table_name).upper(),
            })
        data = {
            "list": table_infos
        }
        Form.to_file(data, "tmp/config.js", "templates/config.template")
