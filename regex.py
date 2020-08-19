#!/usr/bin/env python3
import re

def wildcards_and_classes():
    #the 'r' in the search string indicates it is a "rawstring", meaning that
    #  that the interpreter should not interpret special characters
    print(re.search(r"aza", "plaza"))
    print(re.search(r"aza", "shirt"))
    print(re.search(r"p.ng", "Penguin", re.IGNORECASE))
    print(re.search(r"[Pplython]","Python"))
    print(re.search(r"[a-z]way", "The end of the highway"))
    print(re.search(r"[a-z]way", "what a way to go"))
    print(re.search(r"[^a-zA-z0-9]", "Find the first space"))
    print(re.search(r"[^a-zA-z0-9 ]", "Find the punctuation!"))
    print(re.search(r"this|that", "Will we find that or this?"))
    print(re.findall(r"cat|dog", "I love cats and dogs"))

def repitition():
    print(re.search(r"iss{2}", "Far East Mississippi")) #".*" any number of chars
    print(re.search(r"Py.*n", "Pygmalion"))
    print(re.search(r"Py.*n", "Python Programming")) #demonstrates GREEDY behavior
    print(re.search(r"Py.*?n", "Python Programming")) #demonstrates NON-GREEDY behavior
    print(re.search(r"Py[a-z]*n", "Pyn")) #Demonstrates 0 of class
    print(re.search(r"o+l+","goldfish"))
    print(re.search(r"o+l+","wooly"))
    print(re.search(r"o+l+","boil")) #Does not match because of 'i' between 'o' and 'l'
    print(re.search(r"p?each","To each their own")) #? makes the 'p' optional (0 or 1)

def special_stuff():
    print(re.escape("$$Add backslash to special chars$$"))
    print(re.split(r"[.?!]", "One sentence. Another one? And a thrid!")) #NON-inclusive split on identified characters
    print(re.split(r"([.?!])", "One sentence. Another one? And a thrid!")) #INCLUSIVE split on identified characters
    print(re.sub(r"\bgreen\b", "blue", "This will replace green with blue"))
    print(re.sub(r"[\w.%+-]+@[\w.]+", "[REDACTED]", "Received an email for go_nuts@myexample.com"))
    print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace-, Linda"))# \NUMBER in second parm identifies the groups in expression

def advanced_stuff():
    result = re.search(r"^(\w*), (\w*)", "Lovelace, Linda")#parens identify groups that can be returned
    print(result.groups())
    print("Last name: {}  First name: {}".format(result[1], result[2])) #Notice 1 is first element
    print(re.findall(r"\b[a-zA-Z]{5}\b", "Match words that are five letters in length ")) #/b indidcate word

# wildcards_and_classes()
# repitition()
# special_stuff()
advanced_stuff()
