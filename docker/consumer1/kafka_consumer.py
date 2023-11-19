from kafka import KafkaConsumer
from json import loads
import time

time.sleep(60)

import hdfs

batchsize = 100

try:

    consumer = KafkaConsumer(
        'A',
        bootstrap_servers=['kafka1:9092', 'kafka2:9093', 'kafka3:9094'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

except:
  raise Exception('kafka connect error')


msgs, count = [], 0
for message in consumer:
    msg = str(message.value)
    
    msgs.append(msg)
    count += 1
    
    if count >= batchsize:
      hdfs.write_to_hdfs("\n".join(msgs))
      msgs, count = [], 0
      print("Topic A flush")
    
    