#!/usr/bin/python
import sys
longest_token = 0
longest_line = 0

for line in sys.stdin:                # input from standard input
    line = line.strip()
    tokens = line.split()
    if len(line)>longest_line:
        longest_line = len(line)

    for token in tokens: 
          if len(token) > longest_token:
              longest_token = len(token)
print('longesttoken'+'\t'+str(longest_token))
print('longestline'+'\t'+str(longest_line))
