import os.path
from unittest import TestCase

import pandas

from apply.issue.issure_db_excel.models import MysqlColumns, MysqlTables
from conf.config import localhost_oa_session, DATA_DIR


class TestDbToExcel(TestCase):

    def test_db_to_excel(self):
        db = "oa"
        data = []
        vos = localhost_oa_session.query(MysqlTables).filter(MysqlTables.TABLE_SCHEMA == db).all()
        for vo in vos:
            vos2 = localhost_oa_session.query(MysqlColumns).filter(
                MysqlColumns.TABLE_SCHEMA == db,
                MysqlColumns.TABLE_NAME == vo.TABLE_NAME
            ).order_by(MysqlColumns.TABLE_NAME, MysqlColumns.COLUMN_NAME).all()
            for vo2 in vos2:
                data.append({
                    "表名": vo2.TABLE_NAME,
                    "字段名": vo2.COLUMN_NAME,
                    "注释": vo2.COLUMN_COMMENT,
                    "数据类型": vo2.DATA_TYPE,
                    "主键": vo2.COLUMN_KEY,
                    "可为空": vo2.IS_NULLABLE,
                    "默认值": vo2.COLUMN_DEFAULT,
                    "字符串最大长度": vo2.CHARACTER_MAXIMUM_LENGTH,
                    "数据规模": vo2.NUMERIC_SCALE,
                    "数据精度": vo2.NUMERIC_PRECISION,
                })
        df = pandas.DataFrame(data)
        df.to_excel(os.path.join(DATA_DIR, "oa系统表结构.xlsx"), index=False)
        df.to_csv(os.path.join(DATA_DIR, "oa系统表结构.csv"), index=False)
        df.to_html(os.path.join(DATA_DIR, "oa系统表结构.html"), index=False)
        df.to_json(os.path.join(DATA_DIR, "oa系统表结构.json"), orient="records", force_ascii=False, indent=2)

        # path = 'name.xlsx'
        # writer = pandas.ExcelWriter(path, engine='xlsxwriter')
        # df.to_excel(writer, startrow=1, sheet_name='Sheet1', index=False)
        # workbook = writer.book
        # worksheet = writer.sheets['Sheet1']
        # for i, col in enumerate(df.columns):
        #     column_len = df[col].astype(str).str.len().max()
        #     column_len = max(column_len, len(col)) + 2
        #     worksheet.set_column(i, i, column_len)
        # writer.save()
