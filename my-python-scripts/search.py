import re

text = "My name is Shubham"
pattern = r"name"

search =  re.search(pattern,text)
if search:
    print ("Match found:",search.group())
else:
    print("Match not found")
    