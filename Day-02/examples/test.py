import re

text = "hello how are you man"
pattern = r" "

split1 = re.split(pattern, text)
print("my split is",split1)