#!/usr/bin/python
import sys,re
for line in sys.stdin:
    line=line.strip()
    pattern=re.compile(r"row Id=\"(\d+)\" PostTypeId=\"(\d+)\".*ViewCount=\"(\d+)\"")
    m1=pattern.search(line) ##use RE to search the specific words
    if m1:
        if m1.group(2)=="1":
            questionid=m1.group(1)## RE index is slightly different from python index
            viewcount=m1.group(3)   
            print("{0}\t{1}".format(viewcount, questionid))
