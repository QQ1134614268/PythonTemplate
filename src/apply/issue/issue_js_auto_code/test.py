import os
from unittest import TestCase

from apply.issue.issue_js_auto_code.js_auto_code_v0 import Form
from util.str_util import to_upper_camel, to_snake, to_lower_camel


class TestAutoCode(TestCase):

    def test_run(self):
        table = "organization"
        rows = Form.get_table_info(table, "oa")
        data = {
            "list": rows
        }
        Form.to_file(data, f"{table}.vue", os.path.dirname(__file__), "templates/vue.template")

    def test_run_vue_js(self):
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
        Form.to_file(data, "tmp/routes.js", os.path.dirname(__file__), "templates/routes.template")

    def test_run_config_js(self):
        tables = Form.get_tables("oa")
        table_infos = []
        for table in tables:
            table_name = table["TABLE_NAME"]
            table_infos.append({
                "tableLowerCaml": to_lower_camel(table_name),
                "tableConst": to_snake(table_name).upper(),
            })
        data = {
            "list": table_infos
        }
        Form.to_file(data, "tmp/config.js", os.path.dirname(__file__), "templates/config.template")
