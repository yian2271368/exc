#!/usr/bin/python


list_empty=''
for line in sys.stdin:                 
    line = line.strip()                 
    tokens = line.split()
    for i in range(len(tokens)-2):
        token = tokens[i:i+3]

        print("{0}\t{1}".format(token, 1))
