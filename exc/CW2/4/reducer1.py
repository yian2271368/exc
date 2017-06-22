#!/usr/bin/python
import sys

prev_OwnerUserId = ''
ACanswer_id=''
total_value=0
for line in sys.stdin:
	line=line.strip()
	OwnerUserId, AnswerId, count=line.split('\t')
	count = int(count)
	if prev_OwnerUserId == OwnerUserId:
		ACanswer_id += AnswerId + ', '
		total_value += count
	else:
		if prev_OwnerUserId:
			print '%s\t%s\t%s' % (prev_OwnerUserId, ACanswer_id, total_value)
		ACanswer_id=AnswerId + ', '
		total_value=count
		prev_OwnerUserId=OwnerUserId

if prev_OwnerUserId == OwnerUserId:
	print '%s\t%s\t%s' % (prev_OwnerUserId, ACanswer_id, total_value)
