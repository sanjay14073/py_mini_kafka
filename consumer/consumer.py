# consumer.py
import time
import logging


class Consumer:
    def __init__(self, broker, consumer_id):
        self.broker = broker
        self.consumer_id = consumer_id
        self.topics = set()  # Keeps track of subscribed topics

    def subscribe(self, topic):
        """Subscribe to a topic."""
        self.broker.subscribe(topic, self.consumer_id)
        self.topics.add(topic)
        logging.info(f"Consumer {self.consumer_id} subscribed to {topic}")

    def consume(self, topic):
        """Consume a message from the given topic."""
        message = self.broker.consume(topic, self.consumer_id)
        if message:
            self.process_message(message)
        else:
            logging.error(f"Consumer {self.consumer_id} found no new messages in {topic}")

    def process_message(self, message):
        """Process the consumed message."""

        logging.info(f"[Consumer-{self.consumer_id}] Processed: {message}")

    def start_consuming(self):
        """Start consuming messages from all subscribed topics."""
        while True:
            for topic in self.topics:
                self.consume(topic)
            time.sleep(1) 
