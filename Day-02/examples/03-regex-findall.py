import re

text = "can you get me some water? fill the water into a bottle"
pattern = r"water"

# findall() give All matches in a (list) 
# group() can't be used with findall() because it gives one result object
findall = re.findall(pattern, text)
if findall:
    print("Pattern found:", findall)
else:
    print("Pattern not found")
