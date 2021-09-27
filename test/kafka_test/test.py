# -*- coding:utf-8 -*-
"""
@Time: 2021/7/19
@Description:
"""

import json

from kafka import KafkaConsumer

from conf.kafka_conf import IP, PORT, TOPIC, KEY

consumer = KafkaConsumer(TOPIC, group_id=KEY, bootstrap_servers=["{}:{}".format(IP, PORT)])
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
    mes_str = str(message.value, encoding="utf-8")
    json.loads(mes_str, encoding="utf-8")

    # {
    #     'stk_code': '603995.sh',
    #     'stk_name': '甬金股份',
    #     'anno_date': '2021-06-10',
    #     'again_rz_type': '激励股份授予',
    #     'sell_begin_date': '',
    #     'sell_end_date': '2021-05-07',
    #     'total_sell_num': '5.0000',
    #     'sell_price': '15.1900',
    #     'stk_sort': 'A股',
    #     'sell_sec_code': '603995.sh',
    #     'sell_stk_name': '甬金股份',
    #     'purchase_code1': '',
    #     'purchase_name1': '',
    #     'purchase_code2': '',
    #     'purchase_name2': '',
    #     'actual_fund_raise_total_amt': '75.9500',
    #     'old_shareholder_cfg_rate': '',
    #     'sell_total_shares_before': '23301.7400',
    #     'sell_total_shares_after': '23306.7400',
    #     'sell_tra_shares_before': '',
    #     'sell_tra_shares_after': '',
    #     'add_stock_listed_date': '2021-06-08',
    #     'regist_date': '',
    #     'ex_date': '',
    #     'ex_price': '',
    #     'sell_obj': '激励对象：徐晓东。',
    #     'remarks': '预留限制性股票授予。'
    # }
