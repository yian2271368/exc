#!/usr/bin/python

import sys
max_grade=0
highest_name=''
for line in sys.stdin:
    line=line.strip()
    name,avrg=line.split('\t',1)
    if avrg > max_grade:
        max_grade=avrg
        highest_name=name
print("{0}\t{1}".format(highest_name,max_grade))
