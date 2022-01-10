#!/usr/bin/python3
""" This module displays the header value of
'X-Request-Id' in response from
url passed in cmd """
import sys
import requests

if __name__ == '__main__':
    resp = requests.get(sys.argv[1])
    value = resp.headers.get('X-Request-Id')
    print('{}'.format(value))
