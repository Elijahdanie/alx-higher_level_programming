#!/bin/bash
#takes in a URL, sends a request to that URL, and displays
#the size of the bodyof the response

curl -sL $1 -i | grep Content-Length | cut -d ' ' -f2
