#!/usr/bin/env python3
import os
import csv

starting_dir = os.getcwd()
def csvstuff():
    print("Starting in directory: {}".format(starting_dir))
    os.chdir(starting_dir)

    testdata_fname = 'data/testdata.csv'
    with open(testdata_fname) as csv_f:
        csvreader = csv.reader(csv_f)
        for row in csvreader:
            #Define the 'tuples'
            name, phone, role = row
            print("Name: {}, Phone: {}, Role:{}".format(name, phone, role))

    hosts_fname = 'data/hosts.csv'
    if not os.path.exists(hosts_fname):
        hosts =[["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
        #csv.writer creates a csv record for each list
        with open(hosts_fname, 'w') as hosts_csv:
            writer = csv.writer(hosts_csv)
            writer.writerows(hosts)

    soft_fname = 'data/software.csv'
    print("\nReading csv file as dictionary:")
    with open(soft_fname) as soft_csv:
        reader = csv.DictReader(soft_csv)
        for row in reader:
            print("{} has {} users".format(row["name"], row["users"]))

    dept_fname = 'data/by_department.csv'
    if not os.path.exists(dept_fname):
        users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
            {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
            {"name": "Charlie Grey", "username": "greyc", "department": "development"}]
        keys = ["name", "username", "department"]
        #csv.DictWriter creates a csv file from a dictionary with keys as headers
        with open(dept_fname, 'w') as dept_csv:
            #identify the keys as the column headers
            writer = csv.DictWriter(dept_csv, fieldnames=keys)
            writer.writeheader()
            writer.writerows(users)

csvstuff()
