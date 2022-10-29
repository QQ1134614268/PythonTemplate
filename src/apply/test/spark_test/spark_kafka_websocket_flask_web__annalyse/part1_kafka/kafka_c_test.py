# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:
"""
from kafka import KafkaConsumer

consumer = KafkaConsumer('bigdata', bootstrap_servers=['192.168.147.128:9092'])
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
