#!/usr/bin/python3
"""displays the header X-Request-Id from the response"""
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as resp:
        headers = resp.headers
        print(headers.get('X-Request-Id'))
