chmod +x /home/workspace/src/word_count/mapper.py
chmod +x /home/workspace/src/word_count/reducer.py

hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
    -files /home/workspace/src/word_count/mapper.py,\
/home/workspace/src/word_count/reducer.py,\
/home/workspace/src/word_count/porter.py,\
/home/workspace/src/word_count/text_parser.py,\
/home/workspace/src/word_count/stopwords.txt \
    -mapper mapper.py \
    -reducer reducer.py \
    -input /data/*.txt \
    -output /output/word_count

