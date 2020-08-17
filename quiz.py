#!/usr/bin/env python3
import os
import datetime
import csv
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
# print(os.getcwd())
# dir = os.path.join(os.getcwd(), os.pardir)
# print(os.listdir(dir))
# print(os.path.abspath(dir))

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    #create_file(filename)

    # Open the file
    with open(filename) as file:
    # Read the rows of the file into a dictionary
        reader = csv.DictReader(file)
    # Process each item of the dictionary
        for row in reader:
            color, name, type = row
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string

#Call the function
print(contents_of_file("flowers.csv"))

def skip_header(filename):
    return_string = ""
# Open the file
    with open(filename) as file:
    # Read the rows of the file
        rows = csv.reader(file)
        next(rows)
    # Process each row
        for row in rows:
            one, two, three = row
        # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(one, two, three.strip())
    return return_string

#Call the function
#print(skip_header("flowers.csv"))

with open('flowers.csv') as file:
    lines = csv.reader(file)
    for line in lines:
    # lines.sort()
        print(str(line))
