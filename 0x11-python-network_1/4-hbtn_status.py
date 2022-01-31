#!/usr/bin/python3
""" This module displays content and data type
    of  response from URI In a specialize format"""
import requests

if __name__ == '__main__':
    resp = requests.get('https://intranet.hbtn.io/status')
    data = resp.text
    content = resp.content.decode('utf-8')
    print('Body response:')
    print('\t - type: {}'.format(type(data)))
    print('\t - content: {}'.format(content))
