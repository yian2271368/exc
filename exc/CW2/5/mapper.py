#!/usr/bin/python
##i feel like if i use the algorithm you said in class, the probability will not be the same since it might happen that one mapper has more lines than others.  

import sys, random
from heapq import heappush, heapreplace
H = []
k=1 ## if we want to pick n lines in a mapper, just change the value of k to n.
for line in sys.stdin:
    line=line.strip()
    RNum = random.random()
    if len(H) < k:
        heappush(H, (RNum, line))
    elif RNum > H[0][0]:
        heapreplace(H, (RNum, line))
for Rnum,line in H:
    print ("{0}\t{1}".format(Rnum,line))



###reference:http://had00b.blogspot.co.uk/2013/07/random-subset-in-mapreduce.html
