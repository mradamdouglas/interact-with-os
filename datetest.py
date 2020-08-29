#!/usr/bin/env python3
import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = r"[.?!,;:-']"
  string1 = re.sub(punctuation, " ", string1)
  string2 = re.sub(punctuation, " ", string2)

# print(compare_strings("Have a Great Day!", "Have a great day?")) # True

import datetime
from datetime import date

def add_year(date_obj):
  try:
    new_date_obj = date_obj.replace(year = date_obj.year + 1)
  except ValueError:
    # This gets executed when the above method fails,
    # which means that we're making a Leap Year calculation
    print("Exception add_year")
    new_date_obj = date_obj.replace(year = date_obj.year + 4)
  return new_date_obj

def next_date(date_string):
  # Convert the argument from string to date object
  print("START: date_string: {}  {} ".format(type(date_string), date_string))
  date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
  next_date_obj = add_year(date_obj)
  print("blah blah blah {}".format(next_date_obj))
  # print("Next date: {}".format(str(next_date_obj)))
  # Convert the datetime object to string,
  # in the format of "yyyy-mm-dd"
  next_date_string = next_date_obj.strftime("%Y-%m-%d")
  print("Next date string: {} ".format(next_date_string))
  return next_date_string

today = date.today()  # Get today's date
print(next_date(str(today)))
# Should return a year from today, unless today is Leap Day

print(next_date("2021-01-01")) # Should return 2022-01-01
print(next_date("2020-02-29")) # Should return 2024-02-29
