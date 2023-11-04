# First start Zookeper and Kafka as described here: https://kafka.apache.org/quickstart

# Probably the best tutorial is this one: https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

from kafka import KafkaConsumer

consumer = KafkaConsumer('python')
for message in consumer:
  print(message.topic, ':', message.value.decode())

# For extra consumer features @see https://kafka-python.readthedocs.io/en/master/
