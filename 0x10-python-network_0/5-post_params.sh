#!/bin/bash
#passes variables to te URI passed in and display the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
