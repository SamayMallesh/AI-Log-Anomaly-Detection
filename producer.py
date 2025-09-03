from kafka import KafkaProducer
import time
import csv
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'logs'

with open('../data/sample_logs.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        producer.send(topic, row)
        print(f"Sent: {row}")
        time.sleep(1)  # simulate streaming
