import unittest

from kafka import KafkaConsumer
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
            producer.send(MY_TOPIC1, value=b'hello kafka')
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
