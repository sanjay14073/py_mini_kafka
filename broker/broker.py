## Implementation of Broker Class
from collections import deque, defaultdict
import threading
import logging


class Broker:
    def __init__(self):
        self.topics = defaultdict(deque)
        self.topic_locks = defaultdict(threading.Lock)
        self.consumer_offsets= defaultdict(lambda: defaultdict(int))

    def publish(self,topic,message):
        """Publishes a message to a topic."""
        with self.topic_locks[topic]:
            self.topics[topic].append(message)
            logging.info(f"Published message to topic {topic}: {message}")
            

    def subscribe(self,topic,consumer_id):
        """Subscribes a consumer to a topic (initializes their offset)."""
        if consumer_id not in self.consumer_offsets[topic]:
            self.consumer_offsets[topic][consumer_id] = 0
            print(f"Consumer {consumer_id} subscribed to {topic}")

    def consume(self,topic,consumer_id):
        """Consumes messages from a topic for a specific consumer."""
        with self.topic_locks[topic]:
            offset = self.consumer_offsets[topic][consumer_id]
            if offset < len(self.topics[topic]):
                message = list(self.topics[topic])[offset]
                self.consumer_offsets[topic][consumer_id] += 1
                print(f"Consumer {consumer_id} consumed: {message}")
                return message
            return None