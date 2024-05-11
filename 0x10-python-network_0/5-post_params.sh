#!/bin/bash
# This Bash script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# Variables email and subject are sent with specified values
curl -sX POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
