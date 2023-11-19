# Kafka Data Pipeline Demo

<div style="color: red">WARN: I am running this demo on a laptop with 16GB RAM and Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz and the OS is Ubuntu 22.04, hardware configurations below this are not guaranteed to run the code correctly </div>

### 1. Installation

- install `docker desktop`
- install `docker-compose`
- `pip install jmxquery plotly dash numpy`

### 2. Data

1. download data from `https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data`
2. put `twcs.csv` into `./data`

### 3. Usage

launch docker containers


```bash
cd <YourPath>/Kafka-Pipeline
systemctl --user start docker-desktop
docker network create kafka-network
docker-compose up --build
```

### 4. visualization

kafka-ui: `localhost:8080`
dash: `localhost:8050`
Hadoop HDFS interface: `localhost:9870`
Hadoop cluster interface: `localhost:8088`

### References

[Data-Engineering-Project-with-HDFS-and-Kafka](https://github.com/AhmetFurkanDEMIR/Data-Engineering-Project-with-HDFS-and-Kafka/tree/main)
