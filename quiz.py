#!/usr/bin/env python3
import os
import datetime
def create_python_script(filename):
    comments = "Start of a new Python program.\n"
    with open(filename, "w") as file:
        for i in range(20):
            file.write(comments)
    filesize = os.path.getsize(filename)
    return(filesize)

# print(create_python_script("program.txt"))


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open (filename, "w") as file:
        pass

    # Return the list of files in the new directory
    return os.listdir(os.getcwd())

# print(new_directory("PythonPrograms", "script.py"))

def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        pass
    timestamp = os.path.getmtime(filename)
    print(" {}  {} ".format(timestamp, type(timestamp)))
    ti = datetime.datetime.fromtimestamp(timestamp)
    print(ti)
    # Convert the timestamp into a readable format, then into a strin

    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return ("{}".format(str(ti)[:10]))

#print(file_date("newfile.txt"))
print(os.getcwd())
dir = os.path.join(os.getcwd(), os.pardir)
print(os.listdir(dir))
print(os.path.abspath(dir))
