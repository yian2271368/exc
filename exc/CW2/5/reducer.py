#!/usr/bin/python
import sys
import random
from heapq import heappush, heapreplace
## n mapper will give me n lines ,but since each mapper is assigned with different number of lines, I give a value for each line randomly, and pick the greast value.
H=[]
k=1
for line in sys.stdin:
    line=line.strip()
    num,line=line.split("\t")
    Rum=random.random()
    if len(H)<k:
        heappush(H,(Rum,line))
    elif Rum>H[0][0]:
        heapreplace(H,(Rum,line))
for Rum, line in H:
    print(line)



    
