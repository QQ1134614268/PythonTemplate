import os
from enum import Enum, unique

import jinja2


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
    def get_table_info():
        """SELECT
    TB.TABLE_SCHEMA,    -- 模式
    TB.TABLE_NAME,      -- 表名
    TB.TABLE_COMMENT,   -- 表名注释
    COL.COLUMN_NAME,    -- 字段名
    COL.COLUMN_TYPE,    -- 字段类型
    COL.COLUMN_COMMENT,  -- 字段注释
    COL.DATA_TYPE        -- 字段数据类型
    FROM
        INFORMATION_SCHEMA.TABLES TB,
        INFORMATION_SCHEMA.COLUMNS COL
    Where TB.TABLE_SCHEMA ='gdmo_sp' -- 库名
    AND TB.TABLE_NAME = COL.TABLE_NAME"""
        # 表名,表注释
        # 字段名,字段类型,字段注释, 枚举值

        # json数据 -- class数据-- 类数据
        pass

    @staticmethod
    def table_to_class():
        # 表名,表注释
        # 字段名,字段类型,字段注释, 枚举值

        # json数据 -- class数据-- 类数据
        pass

    @staticmethod
    def class_to_tile():
        resource_dir = os.path.abspath(__file__)
        data2 = {}
        template_file = "template_worker_time.tpl.html"

        template_loader = jinja2.FileSystemLoader(searchpath=resource_dir)
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(template_file)
        output_text = template.render(data2)

    @staticmethod
    def table_to_tile():
        pass


# class User(Form):
#     __table_name__ = ""
#     name = Colum("姓名", "name", StrData(), order=1, nullable=True)
#     age = Colum("年龄", "name", StrData(), order=2, nullable=True)


if __name__ == '__main__':
    pass
