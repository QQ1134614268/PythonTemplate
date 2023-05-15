# -*- coding:utf-8 -*-
"""
@Time: 2022/3/4
@Description:
"""
from kafka import KafkaConsumer

from apply.test.spark_test.spark_kafka_websocket_flask_web__annalyse.spark_kafka_conf import KAFKA_LOCAL

consumer = KafkaConsumer('bigdata', bootstrap_servers=[KAFKA_LOCAL])
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
