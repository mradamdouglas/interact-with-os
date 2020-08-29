#!/usr/bin/env python3.8
import concurrent.futures
import sys
# import argparse
# import os
# import sys
# import logging

rangeVal = 20
useThreadProc = True

'''Threads use a bunch of safety features to avoid having two threads that try to write
to the same variable.  And this means that when using threads, they may end up waiting for
their turn to write to variables for a few milliseconds,
adding up to the small difference between the two approaches. '''

def r_something(name, anyrange, useThreading=True):
    numlist=[]
    print("Range: {}".format(anyrange))
    print("Using {} processing".format("THREADPool" if useThreading else "PROCESSPool"))

    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    executor2 = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    if useThreading:
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
        executor2 = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    for i in range(anyrange):
        executor.submit(process_something, name, i, numlist)

    print("Waiting for all threads to finish")
    print("Let's see if this happens next...")
    print("Long calculation...{}".format(500*45*600*20/50/50/20*30))
    print("Second range: {} to {} ".format(anyrange, anyrange*2))
    for i in range(anyrange, (anyrange*2)+1):
        # executor2.submit(process_something, name, i, numlist)
        process_something(name, i, numlist)
    executor.shutdown()
    executor2.shutdown()
    return numlist

def process_something(name, number, thelist):
    thelist.append(number)
    print(thelist)

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    rangeVal = int(sys.argv[1])

if len(sys.argv) > 2 and sys.argv[2] == "--p":
    useThreadProc = False

returnlist = r_something("George", rangeVal, useThreadProc)
print(returnlist)
prev_val = 0
for val in returnlist:
    if val < prev_val:
        print("Current val {} is less than previous val {}".format(val, prev_val))
    prev_val = val
