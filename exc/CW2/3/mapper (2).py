#!/usr/bin/python
import sys,re
for line in sys.stdin:
    line=line.strip()
    pattern=re.compile(r"row Id=\"(\d+)\".*ParentId=\"(\d+)\".*OwnerUserId=\"(\d+)\"")
    m1=pattern.search(line)
    if m1:
        ownerid=m1.group(3)
        parentid=m1.group(2)
        print("{0}\t{1}".format(ownerid, parentid))
