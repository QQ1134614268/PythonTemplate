import unittest

from kafka import KafkaConsumer
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic

from apply.test.kafka_test.kafka_conf import KAFKA_GGOK, MY_TOPIC1


# todo kafka-python 2.0.2, 2020-09; kafka-python3, 3.0.0 2022-5

class TestKafkaProduce(unittest.TestCase):

    def test_create_topic(self):
        admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_GGOK)
        # 创建topic
        topic = NewTopic(name=MY_TOPIC1, num_partitions=1, replication_factor=1)
        topic_list = [topic]
        ret = admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(ret)

    def test_produce(self):
        producer = KafkaProducer(bootstrap_servers=[KAFKA_GGOK])

        for i in range(0, 2):
            # type(value_bytes) in (bytes, bytearray, memoryview, type(None)
            producer.send(MY_TOPIC1, value=b'lai zi shouke de msg')
        producer.flush()
        producer.close()


class TestKafkaConsumer(unittest.TestCase):

    def test_consumer(self):
        # auto_offset_reset : 'earliest',  'latest
        # group_id
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
