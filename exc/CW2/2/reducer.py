#!/usr/bin/python
import sys

Totalnum=10
value=[]
num = 0
tag=[]


for line in sys.stdin:
    line=line.strip()
    count,ID=line.split("\t")
    count=int(count)
    tag=[count,ID]

    if num<Totalnum:
       value.append(tag)
       num+=1

    else:
       value.sort(key=lambda x: int(x[0]),reverse=True)
       m=value[Totalnum-1][0]
       if count>m:
          del value[Totalnum-1]
          value.append(tag)

value.sort(key=lambda x: int(x[0]),reverse=True)
for i in range(Totalnum):
    print ("{0}\t{1}".format(value[i][0],value[i][1]))
