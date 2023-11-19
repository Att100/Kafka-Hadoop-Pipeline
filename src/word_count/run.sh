chmod +x /home/workspace/src/word_count/mapper.py
chmod +x /home/workspace/src/word_count/reducer.py

hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
    -file /home/workspace/src/word_count/mapper.py -mapper /home/workspace/src/word_count/mapper.py \
    -file /home/workspace/src/word_count/reducer.py -reducer /home/workspace/src/word_count/reducer.py \
    -input /data/*.json \
    -output /home/workspace/output


hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file /home/workspace/src/word_count_test/mapper.py -mapper /home/workspace/src/word_count_test/mapper.py -file /home/workspace/src/word_count_test/reducer.py -reducer /home/workspace/src/word_count_test/reducer.py -input /data/data.txt -output /home/workspace/output/output1