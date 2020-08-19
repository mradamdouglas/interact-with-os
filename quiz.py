#!/usr/bin/env python3
import os
import datetime
import csv
import re
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
# print(contents_of_file("flowers.csv"))

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

# with open('flowers.csv') as file:
#     lines = csv.reader(file)
#     for line in lines:
#     # lines.sort()
        # print(str(line))

def check_web_address(text):
  pattern = ".*\.\w*$"
  result = re.search(pattern, text)
  return result != None
#
# print(check_web_address("gmail.com")) # True
# print(check_web_address("www@google")) # False
# print(check_web_address("www.Coursera.org")) # True
# print(check_web_address("web-address.com/homepage")) # False
# print(check_web_address("My_Favorite-Blog.US")) # True

def check_time(text):
  pattern = "^(1?[0-9])\:[0-5][0-9]\ ?(am|pm|AM|pm)$"
  result = re.search(pattern, text)
  return result != None

# print(check_time("12:45pm")) # True
# print(check_time("9:59 AM")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False


def contains_acronym(text):
  pattern = "\([A-Z0-9].*\)"
  result = re.search(pattern, text)
  return result != None

# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


def check_zip_code (text):
  # result = re.search(r"(?!^)(\d){5,5}(\-(\d){4,4})?", text)
  result = re.search(r" (\d){5,5}(\-(\d){4,4})?", text)
  return result != None

# print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
# print(check_zip_code("90210 is a TV show")) # False
# print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
# print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

def rearrange_name(name):
  result = re.search(r"^(\.*), (\.*)", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

# name=rearrange_name("Kennedy, John F.")
# print(name)


def long_words(text):
  pattern = r"\b[a-zA-Z]{7,}\b"
  result = re.findall(pattern, text)
  return result

# print(long_words("I like to drink coffee in the morning.")) # ['morning']
# print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
# print(long_words("I never drink tea late at night.")) # []
# print(re.findall(r"\b[a-zA-Z]{7,}\b", "I also have a taste for hot chocolate in the afternoon."))

def extract_pid(log_line):
    regex = r"(\[(\d+)\]): (\b[A-Z]+\b)"
    result = re.search(regex, log_line)

    if result is None:
        return None

    print(result.groups())
    return "{} ({})".format(result[1],result[3])

# print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
# print(extract_pid("99 elephants in a [cage]")) # None
# print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
# print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

def transform_record(record):
    new_record = re.sub(r"([\d]{3}-)", r"+1-\1", record, count=1)
    print(re.findall(r"(,[\d]{3})", record))
    print (new_record)
    return new_record
#
# print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# # Sabrina Green,+1-802-867-5309,System Administrator
# print(transform_record("Eli Jones,684-3481127,IT specialist"))
# # Eli Jones,+1-684-3481127,IT specialist
# print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# # Melody Daniels,+1-846-687-7436,Programmer

def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou][aeiou][aeiou]\w*\b"
  result = re.findall(pattern, text)
  #result =re.search(pattern, text)
  return result

# print(multi_vowel_words("Life is beautiful"))
# # ['beautiful']
# print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

def transform_comments(line_of_code):
  result = re.sub(r"#{1,}" ,"//", line_of_code)
  # result = re.findall(r"#{1,}", line_of_code)
  return result

# print(transform_comments("### Start of program"))
# # Should be "// Start of program"
# print(transform_comments("  number = 0   ## Initialize the variable"))
# # Should be "  number = 0   // Initialize the variable"
# print(transform_comments("  number += 1   # Increment the variable"))
# # Should be "  number += 1   // Increment the variable"
# print(transform_comments("  return(number)"))
# Should be "  return(number)"

def convert_phone_number(phone):
    pattern = r"\b([0-9]{3})-([0-9]{3})-([0-9]{4})\b"
    result = re.sub(pattern, r"(\1) \2-\3", phone)
    # result = re.search(pattern, phone)
    # if result != None:
    #   print(result.groups())

    return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
