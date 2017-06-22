#!/usr/bin/python
import sys

max_ACid=''
max_count=0
max_owneruserid=''
for line in sys.stdin:
    line=line.strip()
    owneruserid, Answer_id_list, count = line.split('\t')
    count=count.strip()
    owneruserid=owneruserid.strip()
    Answer_id_list=Answer_id_list.strip()
    count=int(count)
    if count>max_count:
        max_count=count
        max_ACid=Answer_id_list[:-1]
        max_owneruserid=owneruserid
print '%s\t%s\t%s' % (max_count,max_owneruserid,max_ACid)
