#!/usr/bin/python3
"""This module sends a POST request to the URL provided
    With an email as the data"""
import urllib.request
import sys

if __name__ == "__main__":
    if(len(sys.argv) == 3):
        values = {'email': sys.argv[2]}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(sys.argv[1], data)
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            print(data.decode('utf-8'))
