import re

text = "The quick brown fox"
pattern = r"brown"

# re.search()
# 👉 Finds the first match anywhere in the string
search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
