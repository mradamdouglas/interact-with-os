#!/usr/bin/env python3

import sys
import subprocess

filename=sys.argv[1]
with open(filename) as file:
	lines=file.readlines()
	for line in lines:
		oldfile=line.strip()
		newfile=line.strip().replace("jane", "jdoe")
		result = subprocess.run(["mv", oldfile, newfile], capture_output=True)
		print("Oldfile: {}  Newfile: {}".format(oldfile, newfile))
