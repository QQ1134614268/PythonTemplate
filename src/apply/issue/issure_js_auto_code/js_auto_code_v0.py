import os
from enum import Enum
from unittest import TestCase

import jinja2

from apply.issue.issure_js_auto_code.db import DbUtil
from util.str_util import to_lower_camel, to_snake, to_upper_camel


class Colum:
    def __init__(self, name_cn, field_name, data_type=None, comment=None, is_read_mode=None, nullable=None, order=None,
                 regx=None, err_msg=None, is_range=None, is_search=None):
        self.name_cn = name_cn
        self.field_name = field_name
        self.data_type = data_type
        self.is_read_mode = is_read_mode
        self.nullable = nullable
        self.order = order
        self.regx = regx
        self.err_msg = err_msg
        self.comment = comment
        self.is_range = is_range
        self.is_search = is_search


class Data:
    pass


class StrData:
    def __init__(self, length=None, regx=None):
        self.__visit_name__ = "str"
        self.length = length
        self.regx = regx


class IntData:
    def __init__(self, num_min=None, num_max=None):
        self.__visit_name__ = "int"
        self.num_max = num_max
        self.num_min = num_min


class FloatData:
    def __init__(self, num_min=None, num_max=None):
        self.__visit_name__ = "float"
        self.num_max = num_max
        self.num_min = num_min


class DataType(Enum):
    STRING: StrData
    INT: 2
    FLOAT: 4
    BOOL: 8
    TEXT_AREA: 16

    DATE: 32
    TIME: 64
    DATETIME: 128


class Form:

    @staticmethod
    def get_tables(db):
        sql = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = %(db)s"
        db_session = DbUtil("root", "123456", "127.0.0.1", "3306", "oa")
        data = db_session.exec(sql, {"db": db})
        return data

    @staticmethod
    def get_table_info(table_name, db=None):
        # 表名,表注释
        # 字段名,字段类型,字段注释, 枚举值

        # json数据 -- class数据-- 类数据
        sql = """SELECT COL.COLUMN_NAME, COL.COLUMN_TYPE, COL.COLUMN_COMMENT, COL.DATA_TYPE 
        FROM INFORMATION_SCHEMA.COLUMNS COL 
        Where COL.table_schema = %(db)s AND COL.TABLE_NAME = %(table_name)s"""

        db_session = DbUtil("root", "123456", "127.0.0.1", "3306", "oa")
        args = {"db": db, "table_name": table_name}
        data = db_session.exec(sql, args)
        for item in data:
            item["COLUMN_NAME"] = to_lower_camel(item["COLUMN_NAME"])
        return data

    @staticmethod
    def class_to_file(data2, path):
        resource_dir = os.path.dirname(__file__)
        template_file = "autocode.tpl.html"

        template_loader = jinja2.FileSystemLoader(searchpath=resource_dir)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(template_file)
        output_text = template.render(data2)
        with open(path, "w", encoding="utf-8") as f:
            f.write(output_text)

    @staticmethod
    def index_js_to_file2(data2, path, resource_dir=os.path.dirname(__file__), template_file="autocode.tpl.html"):
        template_loader = jinja2.FileSystemLoader(searchpath=resource_dir)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(template_file)
        output_text = template.render(data2)
        with open(path, "w", encoding="utf-8") as f:
            f.write(output_text)


class TestAutoCode(TestCase):

    def test_run(self):
        table = "organization"
        rows = Form.get_table_info(table, "oa")
        data = {
            "list": rows
        }
        Form.class_to_file(data, f"{table}.vue".format(table))

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
            Form.class_to_file(data, f"tmp/{table_upper_caml}.vue")

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
        Form.index_js_to_file2(data, "tmp/index.js", template_file="index.template")
