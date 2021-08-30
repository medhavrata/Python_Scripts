#!/usr/bin/env python3

import requests
import socket

local = ['127.0.0.1']

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    print(localhost)
    if localhost in local:
        return True
    else:
        return False
    #return localhost == 127.0.0.1


def check_connectivity():
    request = requests.get("http://www.google.com")
    print(request.status_code)
    return request.status_code == 200

print(check_localhost())
print(check_connectivity())