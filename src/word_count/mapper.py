#!/usr/bin/env python
import sys
import json

from porter import PorterStemmer
from text_parser import TextParser


parser = TextParser("./stopwords.txt")
stemmer = PorterStemmer()

# input comes from standard input (STDIN)
for line in sys.stdin:
    try:
        # Parse JSON
        record = json.loads(line)
        
        # Extract the desired fields
        tweet_id = record['tweet_id']
        tweet = record['text']
        
        # Text processing
        stem_cache = dict()
        word_counts = dict()
        words = parser.parse(tweet)
        
        for j, word in enumerate(words):
            if word in stem_cache.keys():
                _word = stem_cache[word]
            else:
                _word = stemmer.stem(word)
            if _word not in word_counts.keys(): word_counts[_word] = 0
            word_counts[_word] += 1
        
        # Output the result
        for k, v in word_counts.items():
            print('%s\t%s' % (k, v))
            
    except ValueError as e:
        # Handle error in case of bad data
        continue
