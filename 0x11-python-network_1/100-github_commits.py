#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name, repo_name)
    response = requests.get(url)

    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author_name))
