#!/usr/bin/python
import sys
prev=''
lst1=[]

def prt(studentid,lst1):
    print studentid, '-->',
    for (k,v) in lst1:
        print ("(%s,%s)"%(k,v)),
    print

for line in sys.stdin:
    line=line.strip().split()
    if line[0]==prev:
        if len(line) == 2:
            studentid = line[1]
        if len(line)==3:
            lst1.append((line[1],line[2]))

    else :

        if lst1 :
            prt(studentid,lst1)
        if len(line)==2:
            studentid=line[1]
        lst1=[]
        if len(line)==3:
            lst1.append((line[1], line[2]))
        prev=line[0]
prt(studentid,lst1)
