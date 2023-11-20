# Kafka Hadoop Pipeline Demo

### 1. Installation

- install `docker desktop`
- install `docker-compose`
- `pip install jmxquery plotly dash numpy`

### 2. Data

1. download data from `https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data`
2. put `twcs.csv` into `./data`

### 3. Configuration

- **Kafka**

    + zookeeper
    + brokers: kafka1, kafka2, kafka3

- **Hadoop**
  
    + namenode
    + nodemanager
    + resourcemanager
    + historyserver
    + datanodes: datanode1, datanode2, datanode3

- **Producer**
- **Consumer**

    + consumers: consumer1, consumer2

### 4. Usage

#### 4.1 Start Basic Services

launch docker containers for hadoop and kafka cluster

```bash
cd <YourPath>/Kafka-Pipeline
systemctl --user start docker-desktop
docker network create kafka-network
docker-compose build
chmod +x ./run-kafka-hadoop.sh
./run-kafka-hadoop.sh
```

in new terminal, run

```bash
chmod +x ./modify-env.sh
./modify-env.sh
```

to install python3 for all hadoop nodes, after all kafka and hadoop nodes are set, run

```bash
chmod +x ./run-producer-consumer.sh
./run-producer-consumer.sh
```

in new terminal to start the producer and consumers

#### 4.2 MapReduce Word Count

start mapreduce job in new terminal

```bash
docker exec -it namdenode /bin/bash

# in the opened namenode terminal
cd /home/workspace/src/word_count
chmod +x ./run.sh
./run.sh
```

output should be in file `/output/word_count/part-00000` of the hadoop hdfs

### 5. Visualization

kafka-ui: `localhost:8080`
dash: `localhost:8050`
Hadoop HDFS interface: `localhost:9870`
Hadoop cluster interface: `localhost:8088`

### References

[Data-Engineering-Project-with-HDFS-and-Kafka](https://github.com/AhmetFurkanDEMIR/Data-Engineering-Project-with-HDFS-and-Kafka/tree/main)
