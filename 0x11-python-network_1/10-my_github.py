#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user', auth=(username, password))
    data = response.json()

    if 'id' in data:
        print(data['id'])
    else:
        print(None)
