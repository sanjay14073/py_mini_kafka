
# Mini Kafka-like System in Python

This is a simple implementation of a Kafka-like messaging system using Python and multithreading. It includes basic components such as a `Broker`, `Producer`, and `Consumer`. The system allows producers to publish messages to topics, and consumers to consume messages from these topics.

## Project Structure

```
mini_kafka/
├── broker/
│   ├── __init__.py       # Import Broker here
│   └── broker.py         # Broker class
├── producer/
│   ├── __init__.py
│   └── producer.py       # Producer logic
├── consumer/
│   ├── __init__.py
│   └── consumer.py       # Consumer logic
├── message/
│   ├── __init__.py
│   └── message.py        # (Optional) Message abstraction
└── main.py               # Entry point

```

## Components

1. **Broker**: 
    - Manages topics and stores messages for those topics.
    - Handles publishing messages to topics and allowing consumers to consume from them.

2. **Producer**:
    - Generates messages and publishes them to a specified topic.
    - Simulates message production at a regular interval.

3. **Consumer**:
    - Consumes messages from a specified topic.
    - Simulates message consumption at regular intervals.

4. **Message**:
    - A simple class to define the message structure.

## Requirements

- Python 3.6+
- `logging` package for logging events (used throughout the system).

## Running the System

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/mini-kafka.git
    cd mini-kafka
    ```

2. Run the system:

    ```bash
    python main.py
    ```

3. The system will start with 2 producers and 2 consumers, running for 10 seconds. The producers will send messages to a topic, and the consumers will consume them.

## Key Features

- Producers publish messages to a shared broker.
- Consumers pull messages from the broker and process them.
- Simple logging to track the flow of messages and events.

## Example Logs

When running the system, you will see logs like:

```
2025-05-01 14:45:12,234 - INFO - Producer-0 attempting to publish message to test_topic.
2025-05-01 14:45:13,245 - INFO - Producer-0 successfully published message to test_topic: Message 0 from Producer 0
2025-05-01 14:45:14,256 - INFO - Consumer-0 consumed message: Message 0 from Producer 0
...

