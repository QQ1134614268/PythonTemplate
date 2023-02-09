# -*- coding:utf-8 -*-
"""
@Time: 2021/7/19
@Description:
"""
from kafka import KafkaConsumer

from config.kafka_conf import KAFKA_GGOK, MY_TOPIC1

if __name__ == '__main__':

    consumer = KafkaConsumer(MY_TOPIC1, bootstrap_servers=[KAFKA_GGOK], group_id="group1")

    for message in consumer:
        print({
            "topic": message.topic,
            "partition": message.partition,
            "offset": message.offset,
            "key": message.key,
            "value": message.value,
            "headers": message.headers,
        })
