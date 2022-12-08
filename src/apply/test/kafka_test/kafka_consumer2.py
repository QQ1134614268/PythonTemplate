# -*- coding:utf-8 -*-
"""
@Time: 2021/7/19
@Description:
"""
from kafka import KafkaConsumer

from config.kafka_conf import GGOK_HOST, MY_TOPIC1

if __name__ == '__main__':

    consumer = KafkaConsumer(MY_TOPIC1, bootstrap_servers=[GGOK_HOST], )  # , group_id="KEY"

    for message in consumer:
        print({
            "topic": message.topic,
            "partition": message.partition,
            "offset": message.offset,
            "key": message.key,
            "value": message.value,
            "headers": message.headers,
        })
