#!/usr/bin/env python3
import re
import operator
import sys

error_dict={}
user_dict={}
info_pattern=r"ticky: INFO ([a-zA-Z0-9 ']*) (\[.*)"
error_pattern=r"ticky: ERROR ([a-zA-Z0-0 '']*) (\(.*)"
name_pattern=r"\((\S*)\)$"

def get_errors(input_file):
	with open(input_file) as file:
		reader=file.readlines()
		for record in reader:
			username = get_username(record)
			if username:
				update_user_table(username, record)
				update_error_table(username, record)

def get_username(log_record):
	result=re.search(name_pattern, log_record)
	if result != None:
		name=result.group(1)
		if name not in user_dict:
			user_dict[name] = [0,0]
		return name
	return False

def update_user_table(username, log_record):
	inforec = re.search(info_pattern, log_record)
	if inforec != None:
		user_dict[username][0] += 1
		print(log_record)

def update_error_table(username, log_record):
	errorrec=re.search(error_pattern, log_record)
	if errorrec != None:
		user_dict[username][1] += 1
		error = errorrec.group(1)
		if error not in error_dict:
			error_dict[error] = 0
		error_dict[error] += 1

def sort_dict(in_dict, itemno=0, revOrder=False):
	sorted_dict = sorted(in_dict.items(), key=operator.itemgetter(itemno), reverse=revOrder)
	return sorted_dict

def write_user_report(filename, dictlist):
	keyrec="Username,INFO,ERROR\n"
	with open(filename, "w") as file:
		file.write(keyrec)
		for item in dictlist:
			outrec = "{},{},{}\n".format(item[0],item[1][0], item[1][1])
			file.write(outrec)

def write_error_report(filename, dictlist):
	keyrec="Error,Count\n"
	with open(filename, "w") as file:
		file.write(keyrec)
		for item in dictlist:
			outrec="{},{}\n".format(item[0],item[1])
			file.write(outrec)

get_errors(sys.argv[1])
write_user_report("user_statistics.csv", sort_dict(user_dict, 0, False))
write_error_report("error_message.csv", sort_dict(error_dict, 1, True))
