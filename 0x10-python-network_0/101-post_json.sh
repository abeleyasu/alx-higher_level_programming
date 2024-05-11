#!/bin/bash
# This Bash script sends a JSON POST request to a URL passed as the first argument
# It sends the contents of a file passed as the second argument in the body of the request
# It displays the body of the response
if [ -f "$2" ]; then
    curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
else
    echo "Not a valid JSON"
fi
