#!/bin/bash
#this list all http methods supported by URI passed in
curl -sX OPTIONS $1 -i | grep Allow | awk -F ":" '{print $2}' | cut -d ' ' -f 2-
