import time
import logging

class Message:
    def __init__(self, content, producer_id, topic):
        """
        Initializes a Message object.
        :param content: The actual message content.
        :param producer_id: The ID of the producer generating the message.
        :param topic: The topic to which the message is associated.
        """
        self.content = content
        self.producer_id = producer_id
        self.timestamp = time.time() 
        self.topic = topic

    def serialize(self):
        """
        Serializes the message into a dictionary (could be used for JSON or other formats).
        """
        return {
            "content": self.content,
            "producer_id": self.producer_id,
            "timestamp": self.timestamp,
            "topic": self.topic
        }

    def __str__(self):
        """
        String representation of the message for easy debugging/logging.
        """
        return f"Message from Producer {self.producer_id} to topic '{self.topic}': {self.content} at {self.timestamp}"

    def is_valid(self):
        """
        Validates the message format.
        You can add more validations here, like ensuring non-empty content.
        """
        if not self.content or not self.topic:
            logging.error(f"Message validation failed. Invalid content or topic.")
            return False
        return True
