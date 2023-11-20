#!/usr/bin/env python3
import sys
import io
import re
import sys
import os

dir = os.path.dirname(__file__)
sys.path.append(dir)

from porter import PorterStemmer
from text_parser import TextParser


parser = TextParser(os.path.join(dir, "stopwords.txt"))
stemmer = PorterStemmer()


for line in sys.stdin:
    try:
        stem_cache = dict()
        word_counts = dict()
        words = parser.parse(line)
        
        for j, word in enumerate(words):
            if word in stem_cache.keys():
                _word = stem_cache[word]
            else:
                _word = stemmer.stem(word)
            if _word not in word_counts.keys(): word_counts[_word] = 0
            word_counts[_word] += 1
        
        for k, v in word_counts.items():
            print('%s\t%s' % (k, v))
            
    except ValueError as e:
        continue
