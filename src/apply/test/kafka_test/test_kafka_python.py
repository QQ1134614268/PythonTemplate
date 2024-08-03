import json
import unittest
from datetime import datetime

from kafka import KafkaConsumer, TopicPartition
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic

from apply.test.kafka_test.kafka_conf import KAFKA_LOCAL, MY_TOPIC1


class TestKafkaProduce(unittest.TestCase):

    def test_create_topic(self):
        admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_LOCAL)
        # 创建topic
        topic = NewTopic(name=MY_TOPIC1, num_partitions=1, replication_factor=1)
        topic_list = [topic]
        ret = admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(ret)

    def test_produce(self):
        producer = KafkaProducer(bootstrap_servers=[KAFKA_LOCAL])

        for i in range(0, 2):
            # type(value_bytes) in (bytes, bytearray, memoryview, type(None)
            data = {'name': f'name-{i}', 'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            value = json.dumps(data).encode(encoding='utf-8')
            producer.send(MY_TOPIC1, value=value)
        producer.flush()
        producer.close()


class TestKafkaConsumer(unittest.TestCase):

    def test_consumer(self):
        # auto_offset_reset : 'earliest',  'latest
        # group_id
        consumer = KafkaConsumer(MY_TOPIC1, bootstrap_servers=[KAFKA_LOCAL], group_id="group1")

        for message in consumer:
            print({
                "topic": message.topic,
                "partition": message.partition,
                "offset": message.offset,
                "key": message.key,
                "value": message.value,
                "headers": message.headers,
            })

    def test_consumer_v2(self):
        partitions = [TopicPartition(topic=MY_TOPIC1, partition=i) for i in range(1)]
        consumer = KafkaConsumer(bootstrap_servers=[KAFKA_LOCAL])
        # consumer.subscribe(partitions)
        consumer.assign(partitions)
        # consumer.seek_to_beginning(tp)
        # consumer.seek_to_end(tp)
        # consumer.seek(tp, 100)
        # timestamp = datetime.strptime('2024-07-23 08:00:00', '%Y-%m-%d %H:%M:%S').timestamp() * 1000
        timestamp = int(datetime.now().replace(hour=8, minute=0, second=0, microsecond=0).timestamp() * 1000)
        timestamps = {tp: timestamp for tp in partitions}
        tp_offset_dic = consumer.offsets_for_times(timestamps)
        print(tp_offset_dic)
        for tp, offset_and_timestamp in tp_offset_dic.items():
            consumer.seek(tp, offset_and_timestamp.offset)
        for message in consumer:
            data = json.loads(message.value)
            print(data, message.offset, message.partition)
