#!/usr/bin/python

import sys

prev_ownerID=""
value_total = 0
maxvalue_total = 0
maxuser = ""
answer_list=[]
max_answer=[]
for line in sys.stdin:
    line=line.strip()
    ownerID,answerID=line.split("\t")
    if prev_ownerID==ownerID:
        if answerID not in answer_list:
            answer_list.append(answerID)
            value_total+=1
    else:
        if prev_ownerID:
            if value_total>maxvalue_total:
                maxvalue_total=value_total
                maxuser=prev_ownerID
                max_answer=answer_list
        answer_list=[answerID]
        value_total=1
        prev_ownerID=ownerID
if prev_ownerID==ownerID:
    if value_total>maxvalue_total:
        maxvalue_total=value_total
        maxuser=prev_ownerID
        max_answer=answer_list

print("\n"+maxuser+"\t->", ",".join(max_answer))



