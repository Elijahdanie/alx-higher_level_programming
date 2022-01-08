#!/bin/bash
#displays value of header X-School-User-Id of response from URL passed in
curl -s "{$1}" -X GET -H "X-School-User-Id:98"
