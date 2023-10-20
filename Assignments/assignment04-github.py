# import libraries

import requests
import json

from github import Github
#from config import config as cfg

apikey = "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"

g = Github(apikey)


repo = g.get_repo("https://github.com/Ginafenn/Private.git")
print(repo.clone_url)





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