#!/usr/bin/python
import sys

max_ACid=''
max_count=0
max_owneruserid=''
for line in sys.stdin:
    line=line.strip()
    count, owneruserid, answer_id_list = line.split('\t')
    count=count.strip()
    owneruserid=owneruserid.strip()
    answer_id_list=answer_id_list.strip()
    count=int(count)
    if count>max_count:
        max_count=count
        max_ACid=answer_id_list[:-1]
        max_owneruserid=owneruserid
    
print "%s\t -> %s\t%s" %(max_owneruserid, max_count, max_ACid)
