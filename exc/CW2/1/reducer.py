#!/usr/bin/python

import sys
from heapq import heappush,heapreplace
prev_word = ""
prev_docname = ""
total_value = 0
word = ""
path_list = []
path_count = 0

for line in sys.stdin:  # For ever line in the input from stdin
    line = line.strip()
    tags = line.split("\t")
    word = tags[0]
    path = tags[1]

    if prev_word == word:
        if prev_docname == path:
            path_count += 1
        else:
            if prev_docname:
                total_value += 1
                temp_line = "(" + prev_docname + ", " + str(path_count) + ")"
                heappush(path_list,temp_line)

            path_count = 1
            prev_docname = path

    else:
        if prev_docname:
            total_value += 1
            temp_line = "(" + prev_docname + ", " + str(path_count) + ")"
            heappush(path_list,temp_line)
            prev_docname = ""

        if prev_word:  # write result to stdout
            path_string = ", ".join(path_list)
            path_string = "{" + path_string + "}"
            print("{0} : {1} : {2}".format(prev_word, total_value, path_string))
            path_list = []

        prev_word = word
        prev_docname = path
        path_count = 1
        total_value = 0

if prev_docname == path:
    total_value += 1
    temp_line = "(" + prev_docname + ", " + str(path_count) + ")"
    heappush(path_list,temp_line)
    prev_docname = ""

if prev_word == word:  # Don't forget the last key/value pair
    path_string = ", ".join(path_list)
    path_string = "{" + path_string + "}"
    print("{0} : {1} : {2}".format(prev_word, total_value, path_string))
    path_list = []
