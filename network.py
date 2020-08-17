#!/usr/bin/env python3
import requests
import socket
import os

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        return (localhost == '127.0.0.1')

def check_connectivity():
        result = requests.get("http://www.google.com").status_code
        return(result == 200)

print("check_localhost(): {} ".format(check_localhost()))
print("check_connectivity(): {} ".format(check_connectivity()))
print(help(os))
