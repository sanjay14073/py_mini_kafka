import threading
import time
import logging

class Producer:
    def __init__(self, broker, producer_id):
        self.broker = broker
        self.producer_id = producer_id

    def produce(self, topic, message):
        """Produce a message to a given topic."""
        try:
            # Log the message publication attempt
            logging.info(f"Producer-{self.producer_id} attempting to publish message to {topic}.")
            self.broker.publish(topic, message)
            logging.info(f"Producer-{self.producer_id} successfully published message to {topic}: {message}")
        except Exception as e:
            logging.error(f"Producer-{self.producer_id} failed to publish message to {topic}: {e}")

    def start_producing(self, topic):
        """Simulate the production of messages periodically."""
        while True:
            for i in range(5):
                message = f"Message {i} from Producer {self.producer_id}"
                self.produce(topic, message)
                time.sleep(2) 
