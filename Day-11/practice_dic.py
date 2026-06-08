import requests

response = requests.get("https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls")

full_data = response.json()
#for i in range(len(full_data)): --> this can be used for indexing
    #print(full_data[i]["user"]["login"])
for i in full_data:
    print(i["user"]["login"])
