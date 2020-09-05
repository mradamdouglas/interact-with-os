#!/usr/bin/env python3
'''This program demonstrates a way that data can be read from the input stream 
(sys.stdin) or using input()'''

import sys

def capitalize_using_stdin():
	print("Enter something to capitalize. Hit cntl-c to exit")	
	for line in  sys.stdin:
		sentence = ""
		words = line.split(' ')
		for word in words: 
			sentence += word.capitalize() + ' '
		print (sentence.strip())

def capitalize_single_line(): 
	print("Enter something to capitalize")	
	sentence = input()
	output = ""
	words = sentence.split(' ')
	for word in words: 
	    output += word.capitalize() + ' '
	print ("\n\t" + output.strip())
	
#capitalize_using_stdin()
capitalize_single_line()
