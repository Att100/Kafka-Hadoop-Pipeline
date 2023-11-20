from kafka import KafkaConsumer
from json import loads
import time

time.sleep(60)

batchsize = 100

try:

    consumer = KafkaConsumer(
        'B',
        bootstrap_servers=['kafka1:9092', 'kafka2:9093', 'kafka3:9094'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

except:
  raise Exception('kafka connect error')

from hdfs import InsecureClient
import uuid


client = InsecureClient("http://namenode:9870", user='hdfs')
if 'data' not in client.list('/'):
    client.makedirs("/data")

msgs, count = [], 0
for message in consumer:
    msg = str(message.value)
    
    msgs.append(msg+"\n")
    count += 1
    
    if count >= batchsize:
        with open('./data-temp.txt', 'w') as f:
            f.writelines(msgs)
        client.upload('/data/{}.txt'.format(uuid.uuid1()), './data-temp.txt')
        msgs, count = [], 0
        print("Topic B flush")