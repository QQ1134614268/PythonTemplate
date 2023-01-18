import datetime
import re

from apply.issue.iss_re.coastal_system_models import SysDictType, SysDictDatum
from config.db_conf import test_session_128
from util.log_util import logger

if __name__ == '__main__':
    with open("data.txt", encoding="utf-8") as f:
        for line in f.readlines():
            res = re.search(r"([a-zA-Z]+)\t(\w+)\((.+?)\)", line)
            if res:
                group_code, note, values = res.groups()
                vos = test_session_128.query(SysDictType).filter(SysDictType.dict_type == group_code).all()
                if vos:
                    logger.error(f"""{group_code} 已经存在""")
                else:
                    dicType = SysDictType(
                        dict_name=note,
                        dict_type=group_code,
                        status='0',
                        create_by="admin",
                        create_time=datetime.datetime.now(),
                        update_by="admin",
                        update_time=datetime.datetime.now(),
                        remark=note,
                    )
                    test_session_128.add(dicType)
                    sort = 1
                    for value in values.split(","):
                        val, label = value.split(":")

                        data_vo = SysDictDatum(dict_sort=sort,
                                               dict_label=label.replace(" ", ""),
                                               dict_value=val.replace(" ", ""),
                                               dict_type=group_code,
                                               is_default="N",
                                               status="0",
                                               create_by="admin",
                                               create_time=datetime.datetime.now(),
                                               update_by="admin",
                                               update_time=datetime.datetime.now(),
                                               remark=note
                                               )
                        test_session_128.add(data_vo)
                        sort += 1
        test_session_128.commit()
