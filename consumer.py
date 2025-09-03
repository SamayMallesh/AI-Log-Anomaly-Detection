from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='log-consumers',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    log = message.value
    print(f"Received: {log}")
