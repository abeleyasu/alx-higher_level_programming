#!/bin/bash
# Usage: ./5-post_params.sh <URL>

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

response=$(curl -X POST -d "email=$email&subject=$subject" "$url")
echo "$response"
