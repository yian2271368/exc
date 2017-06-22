#!/usr/bin/python
import sys, random
from heapq import heappush, heapreplace

H=[]
k=100
c=0
with open('webLarge.txt','r+b') as file_object:
    for line in file_object:
        line=line.strip()
        Rnum=random.random()
        if c<k:
            heappush(H,(Rnum,line))
        elif Rnum>H[0][0]:
            heapreplace(H,(Rnum,line))
        c+=1
for Rnum, line in H:
    print("{0}{1}".format(line,"%")) ###this % helps me to count if the printed file has exact k lines. since the screen is small:)



###reference:http://had00b.blogspot.co.uk/2013/07/random-subset-in-mapreduce.html
