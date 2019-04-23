from pprint import pprint as pp
import requests
import json
from getpass import getpass

creds = ()
uid = input('User ID (blank if anonymous): ').strip()
if uid:   # TRUTHY!!!!
    pwd = getpass()
    creds = (uid,pwd)

org = 'au-aist2120-19sp'

# GET organization details
url = f'https://api.github.com/orgs/{org}'
resp = requests.get(url, auth=creds)
#pp(resp)
#print(resp.text)
js = json.loads(resp.text)
#pp(js)
print(js['login'])
print(f"# Public Repos: {js['public_repos']}")

# GET list of repositories
url = f'https://api.github.com/orgs/{org}/repos'
resp = requests.get(url, auth=creds)
js = resp.json() # SAME AS json.loads(resp.text)
#pp(js)
print('REPOSITORIES')
print('------------')
for repo in js:
    #pp(repo)
    repo_name = repo['name']
    print(repo_name)

# GET repository listing
print()
repo = input("Which repo: ")
url = f'https://api.github.com/repos/{org}/{repo}/contents'
resp = requests.get(url, auth=creds)
js = resp.json() # SAME AS json.loads(resp.text)
#pp(js)
for entry in js:
    if entry['type'] == 'dir':
        print(entry['name'], '<DIR>')
    else:
        print(entry['name'])
