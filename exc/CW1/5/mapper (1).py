#!/usr/bin/python

import sys


for line in sys.stdin:
    line= line.strip()
    three_seq,count = line.split("\t")
    
    print("{0}\t{1}".format(count,three_seq))
