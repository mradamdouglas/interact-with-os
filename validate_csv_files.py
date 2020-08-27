#!/usr/bin/env python3
import csv

fname = 'user_statistics.csv'
with open(fname) as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Name: {} INFO: {} ERROR: {}".format(row["Username"], row["INFO"], row["ERROR"]))

fname = 'error_message.csv'
with open(fname) as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Error: {}  Count: {}".format(row["Error"], row["Count"]))
