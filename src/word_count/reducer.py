#!/usr/bin/env python3
import sys

current_key = None
current_value = 0
key = None

# input comes from standard input
for line in sys.stdin:
    line = line.strip()

    # parse the input from mapper.py
    key, value = line.split('\t', 1)

    # convert value to int
    try:
        value = int(value)
    except ValueError:
        continue

    if current_key == key:
        current_value += value
    else:
        if current_key:
            # write result to standard output
            print('%s\t%s' % (current_key, current_value))
        current_value = value
        current_key = key

if current_key == key:
    print('%s\t%s' % (current_key, current_value))
