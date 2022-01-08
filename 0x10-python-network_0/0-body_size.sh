#!/bin/bash
# displays body size of url passed in
curl -sL $1 -i | grep Content-Length | awk '{print $2}'
