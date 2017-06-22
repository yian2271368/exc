#!/usr/bin/python

import sys
bigram=""
list_num=[]
value_total=0
for line in sys.stdin:
    line=line.strip().split()
    token=line[3]
    value=int(line[3])
    if line[0:2] == bigram:
            list_num.append(token)
            value_total+=value
    else:
        if bigram:
              print("{0}\t{1}\t{2}".format(" ".join(bigram)," ".join(list_num),value_total))
           
        bigram=line[0:2]
        list_num=[]
        list_num.append(token)
        value_total=value
print("{0}\t{1}\t{2}".format(" ".join(bigram)," ".join(list_num),value_total))
