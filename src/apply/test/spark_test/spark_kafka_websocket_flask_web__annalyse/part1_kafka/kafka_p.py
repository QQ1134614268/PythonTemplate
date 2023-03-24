# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:
"""
import random
import time

from kafka import KafkaProducer

from config.kafka_conf import KAFKA_GGOK

producer = KafkaProducer(bootstrap_servers=KAFKA_GGOK)

site = ['火车东站', '火车南站', '火车北站']

for i in range(10000):
    zhou1 = random.randint(10, 15)
    zhou2 = random.randint(20, 30)
    zhou3 = random.randint(30, 55)
    zhou4 = random.randint(50, 60)
    zhou5 = random.randint(60, 70)
    zhou6 = random.randint(70, 90)
    zhou7 = random.randint(80, 100)
    che_zhan = random.choice(site)
    s = f"{che_zhan},{zhou1},{zhou2},{zhou3},{zhou4},{zhou5},{zhou6},{zhou7}"
    print(s)
    producer.send('bigdata', bytes(s, encoding="utf8"))
    time.sleep(1)

producer.flush()
producer.close()
print("ok")
