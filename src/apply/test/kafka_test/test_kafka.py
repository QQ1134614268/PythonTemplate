import unittest
from datetime import datetime
from time import sleep

from confluent_kafka import Consumer
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

from config.kafka_conf import KAFKA_GGOK, MY_TOPIC1


class TestKafkaProduce(unittest.TestCase):

    def test_produce(self):
        kafka_produce = Producer({'bootstrap.servers': KAFKA_GGOK})

        def delivery_report(err, msg):
            """ Called once for each message produced to indicate delivery result.
                Triggered by poll() or flush(). """
            if err is not None:
                print('Message delivery failed: {}'.format(err))
            else:
                print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

        for data in range(10):
            # Trigger any available delivery report callbacks from previous produce() calls
            kafka_produce.poll(0)
            # Asynchronously produce a message. The delivery report callback will
            # be triggered from the call to poll() above, or flush() below, when the
            # message has been successfully delivered or failed permanently.
            data_msg = f"{data}-{datetime.now()}"
            print(data_msg)
            kafka_produce.produce(MY_TOPIC1, data_msg.encode('utf-8'), callback=delivery_report)
            sleep(3)

        # Wait for any outstanding messages to be delivered and delivery report
        # callbacks to be triggered.
        kafka_produce.flush()


class TestKafkaConsumer(unittest.TestCase):

    def test_consumer(self):

        c = Consumer({
            'bootstrap.servers': KAFKA_GGOK,
            'group.id': str(datetime.now()),
            'auto.offset.reset': 'earliest'
        })

        c.subscribe([MY_TOPIC1])
        print("start: ")
        while True:
            msg = c.poll(timeout=30)

            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            print('Received message: {}'.format(msg.value().decode('utf-8')))

        c.close()


class TestAdminKafka(unittest.TestCase):

    def test_create_topic(self):

        client = AdminClient({'bootstrap.servers': KAFKA_GGOK})
        new_topics = [NewTopic(MY_TOPIC1, num_partitions=3, replication_factor=1)]
        res = client.create_topics(new_topics)
        for topic, f in res.items():
            try:
                f.result()  # The result itself is None
                print("Topic {} created".format(topic))
            except Exception as e:
                print("Failed to create topic {}: {}".format(topic, e))

    def test_del_topic(self):
        client = AdminClient({'bootstrap.servers': KAFKA_GGOK})

        topics = [MY_TOPIC1]
        res = client.delete_topics(topics, operation_timeout=30)
        for topic, f in res.items():
            try:
                f.result()  # The result itself is None
                print("Topic {} deleted".format(topic))
            except Exception as e:
                print("Failed to delete topic {}: {}".format(topic, e))
