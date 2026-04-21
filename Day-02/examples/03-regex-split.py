import re

text = "apple,banana,orange,grape"
pattern = r","

# -------========================================================================v \ 
# re.split()
# 👉 Splits string based on a pattern
split_result = re.split(pattern, text)
print("Split result:", split_result)
