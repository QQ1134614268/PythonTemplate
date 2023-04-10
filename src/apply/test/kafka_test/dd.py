# -*- coding:utf-8 -*-
"""
@Time: 2021/7/19
@Description:
"""
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic

from config.kafka_conf import KAFKA_GGOK, MY_TOPIC1


def create_topic(client, topic):
    # 创建topic
    topic = NewTopic(name=topic, num_partitions=1, replication_factor=1)
    topic_list = [topic]
    ret = client.create_topics(new_topics=topic_list, validate_only=False)
    print(ret)


if __name__ == '__main__':
    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_GGOK)

    if MY_TOPIC1 not in admin_client.list_topics():
        create_topic(admin_client, MY_TOPIC1)

    producer = KafkaProducer(bootstrap_servers=[KAFKA_GGOK])

    for i in range(0, 2):
        # type(value_bytes) in (bytes, bytearray, memoryview, type(None)
        producer.send(MY_TOPIC1, value=b'lai zi shouke de msg')
    producer.flush()
    producer.close()
