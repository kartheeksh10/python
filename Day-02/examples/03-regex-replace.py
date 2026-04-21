import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

# re.sub() (replace)
# 👉 Replaces matches with something else
new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
