#!/usr/bin/python
import sys,re
AC_list=[]
# read the local file i just download which contains the accepted id
for line in file('AC_list.txt'):
    line = line.strip()
    AC_list.append(line)

for line in sys.stdin:
    line=line.strip()
    pattern=re.compile(r"row Id=\"(\d+)\" PostTypeId=\"2\".*OwnerUserId=\"(\d+)\"")
    m1=pattern.search(line)
    if m1:
        rowid=m1.group(1)
        owneruserid=m1.group(2)
        if rowid in AC_list:
            print '%s\t%s\t%s' % (owneruserid, rowid, 1)
