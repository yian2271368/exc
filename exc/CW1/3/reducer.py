#!/usr/bin/python
import sys
longest_token = 0
longest_line =0
for line in sys.stdin:
    split=line.split()
    if split[0] == "longest_token":
        if int(split[1]) > longest_token:
            longest_token = int(split[1])
    else:
        if int(split[1]) > longest_line:
           longest_line =  int(split[1])
print("{0}\t{1}".format(longest_token, longest_line))
