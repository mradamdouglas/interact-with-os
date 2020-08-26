#!/usr/bin/env python3.7

import os
import sys
import subprocess
import re

acceptinput = "Y"
def environment_variables():
    print("HOME: " + os.environ.get("HOME", ""))
    print("PATH: " + os.environ.get("PATH", ""))
    print("UNASSIGNED: " + os.environ.get("UNASSIGNED", ""))
    print(sys.argv)  ## Prints the program name and the arguments as a list
    if acceptinput != "Y":
        values = input("Input a math equation to be evaulated:")
        try:
            print(values)
            print(eval(values))
        except:
            print("Invalid math equation: " + values)

# enviornment_variables()

def running_subprocesses():
    date = subprocess.run(["date"]) #Saves value AND displays value
    print("Type of subprocess.date: " + str(type(date)) + " Value as saved: " +  str(date))
    # subprocess.run(["sleep", '2']) ## Sleeps for two seconds
    subprocess.run(["ls", "-l", "data"], capture_output=False)

    #capture_output requires Python 3.7+
    nofile= subprocess.run(["ls", "nonexistentfie.txt"], capture_output=True)
    print("\nValue of nofile: {}. Return code of ls: {}".format(nofile, nofile.returncode))
    print(nofile.stdout)
    print(nofile.stderr)

    #capture_output requires Python 3.7+
    result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
    print("\nReturn code of host lookup: {}".format(result.returncode))
    #result.stdout returns the captured output as a byte string and shows non-print chars
    print(result.stdout)
    #decode() decodes the captured output as UTF-8
    print(result.stdout.decode().split())

# running_subprocesses()

def setting_environments():
    #Copy the system environment variables
    my_env = os.environ.copy()
    #Adds a new path the copy of the PATH environment
    my_env["PATH"] = os.pathsep.join(["/home/adouglasx/repos/python-practice", my_env["PATH"]])
    #Executes the helloworld.py script using the copy of the environment
    result = subprocess.run(["helloworld.py"], env=my_env)

# setting_environments()

def read_logfiles(file):
    pattern = r"(.*\((\w+)\)$)"
    pat = re.compile(pattern)
    print(str(pat))

    if os.path.exists(file):
        with open(file) as f:
            for line in f:
                # if "CRON" not in f:
                #     continue
                result = re.search(pat, line)
                if result != None:
                    # print(result.group(1))
                    print("Line: {}  Para: {}".format(str(result.group(1).strip()), result.group(2)))

#the sample file used here is not an ideal log file
# read_logfiles("/var/log/mintsystem.log")

print("\nEntering '$?' on the command line will display the exit code. NOTE: Don't sweat the 'command not found' message")
sys.exit(3)
