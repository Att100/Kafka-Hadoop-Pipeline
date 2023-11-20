from json import dumps, loads
from kafka import KafkaProducer
import time
import random
import pandas as pd

time.sleep(40)

try:

  producer = KafkaProducer(bootstrap_servers=['kafka1:9092', 'kafka2:9093', 'kafka3:9094'],
                          value_serializer=lambda x: dumps(x).encode('utf-8'))

except: 
  raise Exception('kafka connect error')



for chunk in pd.read_csv("data/twcs.csv", chunksize=5, skiprows=0, nrows=500000):
    msgs = chunk.to_dict(orient='records')
    random.shuffle(msgs)
    
    for msg in msgs:
        time.sleep(random.randint(0, 100) * 0.001)
        producer.send(random.choice(['A', 'B']), value=msg["text"])
        # print(msg)