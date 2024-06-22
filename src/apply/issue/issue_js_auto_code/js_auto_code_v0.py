import jinja2

from apply.issue.issue_js_auto_code.db_util import res_to_dict
from apply.issue.issue_js_auto_code.model import MysqlColumns, JsForm
from config.db_conf import localhost_oa_engine
from config.db_conf import localhost_test_session, localhost_oa_session
from util.str_util import to_lower_camel


class Form:

    @staticmethod
    def get_tables(db):
        sql = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = %(db)s"
        res = localhost_oa_engine.execute(sql, {"db": db})
        return res_to_dict(res)

    @staticmethod
    def get_columns():
        vos = localhost_oa_session.query(MysqlColumns).filter(
            MysqlColumns.TABLE_SCHEMA == "oa",
            MysqlColumns.TABLE_NAME == "user"
        ).all()
        print(vos)

    @staticmethod
    def get_js_form():
        # Base.metadata.create_all(localhost_test_engine)
        # Base.metadata.drop_all(localhost_test_engine)
        vos = localhost_test_session.query(JsForm).filter(JsForm.TABLE_NAME == "oa").all()
        print(vos)

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


if __name__ == '__main__':
    Form.get_columns()
