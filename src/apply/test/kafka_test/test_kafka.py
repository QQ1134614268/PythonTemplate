import unittest
from datetime import datetime
from time import sleep

from confluent_kafka import Consumer
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

from apply.test.kafka_test.kafka_conf import MY_TOPIC1, KAFKA_LOCAL


class TestKafkaProduce(unittest.TestCase):

    def test_produce(self):
        kafka_produce = Producer({'bootstrap.servers': KAFKA_LOCAL})
        for index in range(10):
            kafka_produce.produce(MY_TOPIC1, f"{index}-{datetime.now()}", callback=lambda err, msg: print(err, msg))
            sleep(3)
        kafka_produce.flush()


class TestKafkaConsumer(unittest.TestCase):

    def test_consumer(self):
        kafka_consumer = Consumer({
            'bootstrap.servers': KAFKA_LOCAL,
            'group.id': str(datetime.now()),
            'auto.offset.reset': 'latest',
        })
        print(kafka_consumer.list_topics().topics)
        kafka_consumer.subscribe([MY_TOPIC1])
        while True:
            message = kafka_consumer.poll(timeout=30)
            if message is None:
                continue
            if message.error():
                print("Consumer error: {}".format(message.error()))
                continue
            print({
                "topic": message.topic(),
                "partition": message.partition(),
                "offset": message.offset(),
                "key": message.key(),
                "value": message.value(),
                "headers": message.headers(),
            })
        kafka_consumer.close()


class TestAdminKafka(unittest.TestCase):
    def test_create_topic(self):
        client = AdminClient({'bootstrap.servers': KAFKA_LOCAL})
        topic_list = [NewTopic(MY_TOPIC1, num_partitions=3, replication_factor=1)]
        res = client.create_topics(topic_list)
        print(res)
        # for topic, f in res.items():
        #     try:
        #         f.result()  # The result itself is None
        #         print("Topic {} created".format(topic))
        #     except Exception as e:
        #         print("Failed to create topic {}: {}".format(topic, e))

    def test_del_topic(self):
        client = AdminClient({'bootstrap.servers': KAFKA_LOCAL})
        topic_list = [MY_TOPIC1]
        res = client.delete_topics(topic_list, operation_timeout=30)
        print(res)
