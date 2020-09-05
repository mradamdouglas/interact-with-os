#!/usr/bin/env python3.6
import random
import sys
import memory_profiler 

@profile
def get_random():
	value = random.randint(0,3)
	print('random_return.py exit code: ' + str(value))
	return value

exval = get_random()
sys.exit(exval)
