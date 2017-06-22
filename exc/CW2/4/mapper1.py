#!/usr/bin/python
import sys,re
for line in sys.stdin:
    line=line.strip()
    pattern=re.compile(r"row Id=\"(\d+)\" PostTypeId=\"(\d+)\".*AcceptedAnswerId=\"(\d+)\"")
    m1=pattern.search(line)
    if m1:
        acceptedid=m1.group(3)
        print '%s' %(acceptedid)
