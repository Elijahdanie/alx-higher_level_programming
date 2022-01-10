#!/usr/bin/python3
"""this module sends a POST request to the URL
    passed in the cmd """
import requests
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    resp = requests.post(sys.argv[1], data)
    print(resp.text)
