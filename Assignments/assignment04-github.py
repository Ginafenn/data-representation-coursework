# import libraries
import requests
import json
from github import Github
from config import config as cfg

# Access the GitHub API using your access token
apikey = cfg["api_key"]
g = Github(apikey)

# List the names of your repositories
for repo in g.get_user().get_repos():
    print(repo.name)


#repo = g.get_repo("https://github.com/Ginafenn/Private.git")
#print(repo.clone_url)

#



#user = g.get_user()

#repos = user.get_repos()

#for repo in repos:
    #print(repo.name)

#filename = "repos-private.json"


#url = 'https://github.com/Ginafenn/Private.git'

#response = requests.get(url, auth = ('token', apikey))
#print (response.status_code)


#with open(filename, "w") as fp:
    #reppJSON = response.json()
    #json.dump(reppJSON, fp , indent=4)