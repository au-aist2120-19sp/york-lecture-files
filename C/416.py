from pprint import pprint as pp
import requests
import json
from getpass import getpass

#url = 'https://api.github.com/'
#resp = requests.get(url)
#pp(resp)
#print(resp.content)

# Ask for credentials
creds=()
uid = input('Enter user id (blank if anonymous): ').strip()
if uid:   # TRUTHY!!!!!! ??????
    pwd = getpass()
    creds=(uid,pwd)

# GET some info about our organization
org = 'au-aist2120-19sp'
url = f'https://api.github.com/orgs/{org}'
resp = requests.get(url, auth=creds)
json_text = resp.content
org_data = json.loads(json_text)
#pp(org_data)
print(f"{org} has {org_data['public_repos']} public repositories")

# GET list of repos for my org
print()
print('REPOSITORIES')
print('------------')
url = f'https://api.github.com/orgs/{org}/repos'
resp = requests.get(url, auth=creds)
# json_text = resp.content
# org_data = json.loads(json_text)
repo_list = resp.json()
#pp(repo_list)
for repo in repo_list:
    print('*', repo['name'])


# GET list of contents of specified repo
print()
repo_name = input("Which repo: ")
url = f'https://api.github.com/repos/{org}/{repo_name}/contents'
resp = requests.get(url, auth=creds)
item_list = resp.json()
#pp(item_list)
for item in item_list:
    print(item['name'])
