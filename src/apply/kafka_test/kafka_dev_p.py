# -*- coding:utf-8 -*-
"""
@Time: 2021/7/19
@Description:
"""
from kafka import KafkaProducer

from kafka.admin import KafkaAdminClient, NewTopic


def create_topics(client):
    topic = NewTopic(name="MY_TOPIC1", num_partitions=1, replication_factor=1)
    topic_list = [topic]
    ret = client.create_topics(new_topics=topic_list, validate_only=False)
    print(ret)


if __name__ == '__main__':
    admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092")
    # create_topics(admin_client)

    producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])

    for i in range(0, 2):
        # type(value_bytes) in (bytes, bytearray, memoryview, type(None)
        producer.send('MY_TOPIC1', value=b'lai zi shouke de msg')
    producer.flush()
    producer.close()
