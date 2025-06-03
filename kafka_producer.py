from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']

while True:
    data = {
        'user_id': random.randint(1000, 9999),
        'product': random.choice(products),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    producer.send('product_clicks', value=data)
    print(f"Sent: {data}")
    time.sleep(2)
