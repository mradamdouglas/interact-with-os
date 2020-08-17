#! /usr/bin/env python3
import os
import datetime
import csv

starting_dir = os.getcwd()

def filestuff():
    input_file_name = 'spider.txt'
    txtfile = open(input_file_name)
    print('Readline: ')
    print(txtfile.readline())
    print('Read:')
    print(txtfile.read())
    txtfile.close()

    print('Using "with" file.open, the file gets auto closed after use')
    with open(input_file_name) as file:
        for line in file:
            #strip() removes the non-print chars like newline and line return
            print(line.upper().strip())

    print('\nSort the lines in the file:')
    with open(input_file_name) as file:
        lines = file.readlines()
        lines.sort()
        print(lines)

    with open("novel.txt", "w") as file:
        file.write("It was a dark and stormy night...\n")
    print("{} filesize: {}".format("novel.txt", os.path.getsize('novel.txt')))

    os.rename("novel.txt", "finalwork.txt")
    #os.remove("novel.txt")
    print("\nDoes 'finalwork.txt' exist?: " + str(os.path.exists("finalwork.txt")))

    print("File size: {}\n".format(os.path.getsize(input_file_name)))
    timestamp = os.path.getmtime(input_file_name)
    print("Modified time(Unix time): {}".format(timestamp))
    print("Modified time(With datetime function): {}\n".
        format(datetime.datetime.fromtimestamp(timestamp)))

    abspath = os.path.abspath(input_file_name)
    print("absolute path: {}".format(abspath))
    relpath = os.path.relpath(input_file_name)
    print("relative path: {}".format(relpath))
    currdir = os.getcwd()
    print("current working directory: {}".format(currdir))
    #os.path.join ensures that the correct separator is used regardless of OS
    print("Joined path: {}\n".format(os.path.join(currdir,input_file_name)))

    if not os.path.exists("new_dir"):
        os.mkdir("new_dir")
    os.chdir("new_dir")
    print(os.getcwd())

    if not os.path.exists("newer_dir"):
        os.mkdir("newer_dir")
    dirtree = os.listdir(os.getcwd())
    print("Items in current directory: {}".format(str(dirtree)))
    for item in dirtree:
        if os.path.isfile(item):
            print("\t{} is a file.".format(item))
        else:
            print("\t{} is a directory.".format(item))

#filestuff()
print("Starting in directory: {}".format(starting_dir))
os.chdir(starting_dir)

testdata_fname = 'testdata.csv'
with open(testdata_fname) as csv_f:
    csvreader = csv.reader(csv_f)
    for row in csvreader:
        name, phone, role = row
        print("Name: {}, Phone: {}, Role:{}".format(name, phone, role))

hosts_fname = 'hosts.csv'
if not os.path.exists(hosts_fname):
    hosts =[["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
    with open(hosts_fname, 'w') as hosts_csv:
        writer = csv.writer(hosts_fname)
        writer.writerows(hosts)
else:
    os.remove(hosts_fname)
