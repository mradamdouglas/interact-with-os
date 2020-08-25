#!/usr/bin/env python3

import sys

for line in  sys.stdin:
	sentence = ""
	words = line.split(' ')
	for word in words: 
		sentence += word.capitalize() + ' '
	print (sentence.strip())
	
