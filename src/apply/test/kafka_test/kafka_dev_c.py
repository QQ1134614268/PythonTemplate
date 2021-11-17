# -*- coding:utf-8 -*-
"""
@Time: 2021/7/19
@Description:
"""
from kafka import KafkaConsumer

if __name__ == '__main__':

    consumer = KafkaConsumer('MY_TOPIC1', bootstrap_servers=['localhost:9092'], )  # , group_id="KEY"

    for message in consumer:
        print("%s:%d:%d: key=%s value=%s headers=%s" % (message.topic, message.partition, message.offset, message.key,
                                                        message.value, message.headers))
