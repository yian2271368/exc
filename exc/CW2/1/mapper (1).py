#!/usr/bin/env python

import sys, os

for line in sys.stdin:
    line=line.strip()
    tokens=line.split()
    shortname=os.environ["mapreduce_map_input_file"].split('/')[-1]# got the short doc name
    for token in tokens:
        print("{0}\t{1}".format(token, shortname))
