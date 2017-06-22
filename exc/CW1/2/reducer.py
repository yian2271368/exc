#! /usr/bin/python
import sys

prev_line=""
value_total = 0
coming_line= ""

for line in sys.stdin:          # For ever line in the input from stdin
    coming_line = line.strip()         # Remove trailing characters
    coming_line, value = line.split("\t", 1)
    value = int(value)


    if prev_line == coming_line:
        value_total += value
    else:

        if prev_line and value_total==1:  
            print("{0}\t".format(prev_line))
        value_total = 1
        prev_line = coming_line

if prev_line == coming_line and value_total==1:  # Don't forget the last key/value pair
    print("{0}".format(prev_line))
