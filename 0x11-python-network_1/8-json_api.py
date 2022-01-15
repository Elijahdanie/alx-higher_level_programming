#!/usr/bin/python3
"""this searches for specified user and prints
   the values of ir and name of json returned
"""
from json.decoder import JSONDecodeError
import requests
import sys

if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': inp}
    resp = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        jdata = resp.json()
        if len(jdata.keys()) > 0:
            print("[{}] {}".format(jdata['id'], jdata['name']))
        else:
            print("No result")
    except JSONDecodeError:
        print("Not a valid JSON")
