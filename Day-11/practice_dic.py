import requests

response = requests.get("https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls")

full_data = response.json()
pr_count ={}
#for i in range(len(full_data)): --> this can be used for indexing
    #print(full_data[i]["user"]["login"])
for i in full_data:
    username=i["user"]["login"]
    if username in pr_count:
        pr_count[username] +=1
    else:
        pr_count[username] = 1
    #print(username)
    #pr_count[username]=pr_count.get(username,0) + 1
    for user, count in pr_count.items():
        print(f"{user}:{count}")

