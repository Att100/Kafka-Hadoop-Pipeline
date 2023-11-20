#!/bin/bash
containers=(datanode1 datanode2 datanode3 namenode nodemanager resourcemanager historyserver)

for container in "${containers[@]}"; do
    docker exec -it "$container" chmod +x /home/workspace/modifications/modify-env.sh
    docker exec -it "$container" sh /home/workspace/modifications/modify-env.sh
done
