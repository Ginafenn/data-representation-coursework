# import libraries

import requests
import json

# Url for CSO exchequer account (historical series)
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Return
def getAll():
    response = requests.get(url)
    return response.json()

# Save into cso.json file
if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)