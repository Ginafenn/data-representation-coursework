# import libraries
import requests
import json
import re
from github import Github
from config import config as cfg

# Going to the config file to get Key
apikey = cfg["api_key"]

g = Github(apikey)

# Repository detail
Owner = 'Ginafenn'
Name = 'Private'
Path = 'Names.txt'
changeData = 'Regina'



repo = g.get_user(Owner).get_repo(Name)


# Retrieving file details
contents = repo.get_contents(Path)
data = contents.decoded_content.decode('utf-8')

# Everytime you see Andrew replace with Regina
data = re.sub(r'Andrew', Name, data)

# Doing a commit and Push
repo.update_file(Path, f"Update 'Andrew' to '{changeData}'", data, contents.sha)

# Printing out Data replaced to ensure working
print("Data replaced")