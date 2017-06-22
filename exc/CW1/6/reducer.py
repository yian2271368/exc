#!/usr/bin/python

import math
import sys

for line in sys.stdin:
    line = line.strip().split()
    str_name=line[0]+" "+line[1]
    xx = line[len(line)-1]
    total_value=int(xx)
    extro = 0.0

    for i in range(2,3):
        num = float(line[i])
        temp = (num)/(float(total_value))
        extro += temp*(float(math.log(temp,2.0)))
       
    if extro == 0.0:
       print("{0}\t{1}".format(str_name,0.0))

    else:
        print("{0}\t{1}".format(str_name,extro*(-1)))



