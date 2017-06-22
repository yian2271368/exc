#!/usr/bin/python
import sys
for line in sys.stdin:

    line=line.strip().split()
    list1=[]

    total_sum = 0

    avrg_grade = 0
    if len(line)!=0:
      if len(line)>5:
        for i in range(2,len(line)):
            mark=line[i][1:(len(line[i])-1)]
            mark=mark.split(',')         ######spilt things
            list1.append(mark[1])
        for i in range(len(list1)):
            total_sum = total_sum + int(list1[i]) ## compute the totaly grade
            avrg_grade = float(total_sum)/float(len(list1))
        print ('{0}\t{1}'.format(line[0],avrg_grade))   ## present the averge grade
