import logging
import threading
from broker import Broker
from producer import Producer
from consumer import Consumer
import time


# Initialize Broker
broker = Broker()

# We define a topic name for the test
topic_name = "test_topic"

# Function to start producer threads
def start_producer_threads():
    for i in range(2):  # Let's create producer threads
        producer = Producer(broker, producer_id=i)
        t = threading.Thread(target=producer.start_producing, args=(topic_name,))
        t.start()

# Function to start consumer threads
def start_consumer_threads():
    consumers = []
    for i in range(2):  # Let's create  consumer threads
        consumer = Consumer(broker, consumer_id=i)
        consumer.subscribe(topic_name)  # Subscribe to the topic
        t = threading.Thread(target=consumer.start_consuming)
        consumers.append(t)
        t.start()

# Entry point for the application main.py
# This is where the program starts executing
if __name__ == "__main__":
    # Set up logging configuration (this can be done globally or in main.py)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    logging.info("Starting the Kafka-like mini system...")

    # Start the producer and consumer threads
    start_producer_threads()
    start_consumer_threads()

