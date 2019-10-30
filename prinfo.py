#!/usr/bin/env python
# encoding=utf8

import requests
import getpass
import argparse

# Define Parameters
Owner = 'alenaPy'
Repo = 'devops_lab'
User = ''
Pass = ''

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--user', required=True, help='User name.')
parser.add_argument('-r', '--repo', required=False, help='Repo name')
parser.add_argument('-a', '--action', required=True, help='Type of info: '
                    '"timestamp" - Opened PR timestamp, '
                    '"title" - Title of opened PR, '
                    '"url" - List of pull requests, '
                    'If not specified, help displayed')
parser.add_argument("-v", "--version", action="version", version="version 3.2.1")
args = parser.parse_args()
User = args.user
Repo = Repo or args.repo
Action = args.action
Pass = getpass.getpass(prompt="Input GitHub User's password:")
# for test use only
# print('********', Owner, Repo, User, Action, '********')
getstring = 'https://api.github.com/repos/' + Owner + '/' + Repo + '/pulls'
data = requests.get(getstring, auth=(User, Pass)).json()
for it in data:
    if it['user']['login'] == User and not it['closed_at']:
        if Action == 'timestamp':
            # get Opened PR timestamp of user User.  
            print('Timestamp opened PR of user', User, it['created_at'])
        elif Action == 'title':
            # get Title of opened PR of user User. 
            print('Title of opened PR of user', User, it['title'])
        elif Action == 'url':
            # get URL of opened PR of user User. 
            print('URL of opened PR of user', User, it['url'])
