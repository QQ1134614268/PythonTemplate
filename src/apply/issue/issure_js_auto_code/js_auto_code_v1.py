from unittest import TestCase

from apply.issue.issure_js_auto_code.model import MysqlColumns, JsForm
from config.db_conf import localhost_test_session, localhost_oa_session


class TestAutoCode(TestCase):

    def test_run(self):
        vos = localhost_oa_session.query(MysqlColumns).filter(
            MysqlColumns.TABLE_SCHEMA == "oa",
            MysqlColumns.TABLE_NAME == "user"
        ).all()
        print(vos)

    def test_run2(self):
        vos = localhost_oa_session.query(MysqlColumns).filter(
            MysqlColumns.TABLE_SCHEMA == "oa",
            MysqlColumns.TABLE_NAME == "user"
        ).all()
        print(vos)

        # Base.metadata.create_all(localhost_test_engine)
        # Base.metadata.drop_all(localhost_test_engine)
        vos = localhost_test_session.query(JsForm).filter(JsForm.TABLE_NAME == "oa").all()
        print(vos)
