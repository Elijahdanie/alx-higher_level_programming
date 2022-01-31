#!/usr/bin/python3
"""
This prints error code from response or content
of the webpage queried
"""

import requests
import sys

if __name__ == '__main__':
    resp = requests.get(sys.argv[1])
    if resp.status_code < 400:
        print(resp.text)
    else:
        print('Error code: {}'.format(resp.status_code))
