# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:
"""
from kafka import KafkaConsumer

from config.kafka_conf import KAFKA_GGOK

consumer = KafkaConsumer('bigdata', bootstrap_servers=[KAFKA_GGOK])
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
