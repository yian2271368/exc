#!/usr/bin/python

import sys

count=0

for line in sys.stdin: 
    line =line.strip()
    value,sequence=line.split("\t")
    count+=1
    if count<21:
        print("{0}\t{1}".format(value,sequence))

