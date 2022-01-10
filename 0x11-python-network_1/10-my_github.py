#!/usr/bin/python3
"""
This module gets github credentials and display te id
"""
import requests
import sys

if __name__ == "__main__":
    try:
        auth = (sys.argv[1], sys.argv[2])
        resp = requests.get('https://api.github.com/user', auth)
        jdata = resp.json()
        print(jdata['id'])
    except BaseException:
        print("None")
