#!/usr/bin/python3

import sys
import glob
def try_catch(file):
    try:
        with open(file) as f:
            print(f.read())
    except:
        print("Exception thrown:  You got an error bruh...")

# try_catch("nonexisting.file")

def validate_user(username, minlen):

    assert type(username) == str, "Assert error: username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalpha():
        return False
    return True

# username=""
# minval=6
# for num, val in enumerate(sys.argv):
#     print("argument {}: {}".format(num, val))
# try:
#     username = sys.argv[1]
#     minval = int(sys.argv[2])
# except:
#     print("system argument for username was not provided")
# finally:
#     print(validate_user(username, minval))

def RemoveValue(my_list, myVal):
    my_list.remove(myVal)
    return my_list
# my_list = [27, 5, 9, 6, 8]
# print(RemoveValue(my_list, 27))

def list_files():
    filelist = (glob.glob("/home/adouglasx/repos/interact-with-os/*.py, recursive=False ))
    for file in filelist:
        print(file)

list_files()
