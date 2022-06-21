# -*- coding:utf-8 -*-
"""
@Time: 2021/7/19
@Description:
"""
import json

from kafka import TopicPartition, KafkaConsumer


def get_kafka_reviews():
    topic = 'credit.csf.rzrq_guarantee_daily'
    total = 10
    consumer = KafkaConsumer(topic, bootstrap_servers=['127.0.0.1:9092'], auto_offset_reset='earliest',
                             enable_auto_commit=False)  # , group_id="KEY"
    partition = TopicPartition(topic, 0)
    _offsets = consumer.end_offsets([partition])
    max_offset = _offsets.get(partition)
    # consumer.assign([partition])
    # start = max_offset - total
    # consumer.seek(partition, start)
    consumer.seek(partition, 0)
    ret = []
    for message in consumer:
        # print('topic: %s, partition: %d, offset: %d, key: %s, value: %s' % (
        #     message.topic, message.partition, message.offset, message.key, message.value))
        ret.append(json.loads(str(message.value, encoding="utf-8")))
        if message.offset + 1 == max_offset:
            break
    return ret


if __name__ == '__main__':
    res = get_kafka_reviews()
