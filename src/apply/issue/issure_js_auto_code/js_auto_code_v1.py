from unittest import TestCase

from apply.issue.issure_js_auto_code.config import localhost_oa_session, localhost_test_session
from apply.issue.issure_js_auto_code.model import MysqlColumns, JsForm


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

        # Base.metadata.create_all(localhost_test_engine)
        # Base.metadata.drop_all(localhost_test_engine)
        vos = localhost_test_session.query(JsForm).filter(JsForm.TABLE_NAME == "oa").all()
        print(vos)
