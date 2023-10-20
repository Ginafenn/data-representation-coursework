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
Path = 'test.txt'
changeData = 'Regina'


# Go to the repository
repo = g.get_user(Owner).get_repo(Name)


# Retrieving file details
file_contents = repo.get_contents(Path)
file_data = file_contents.decoded_content.decode('utf-8')

# Everytime you see Andrew replace with Regina
file_data = re.sub(r'Andrew', Name, file_data)

# DOing a commit and Push
repo.update_file(Path, f"Update 'Andrew' to '{changeData}'", file_data, file_contents.sha)

# Printing out Data replaced to show the task has been completed
print("Data replaced")