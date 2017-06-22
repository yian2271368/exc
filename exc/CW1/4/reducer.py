#!/usr/bin/python
import sys

prev_line = ''
value_total = 0
token=''

for line in sys.stdin:
    line = line.strip()
    token, value = line.split('\t',1)
    value = int(value)
    if prev_line == token:
        value_total += value
    else:
        if prev_line: #send to stdout
            print("{0}\t{1}".format(prev_line, value_total))
        value_total = value
        prev_line = token

print("{0}\t{1}".format(prev_line, value_total))
