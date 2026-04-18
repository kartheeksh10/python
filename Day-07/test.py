import sys

type = sys.argv[1]

if type == "t2.micro":
    print("this will charge 2 dollors")
elif type == "t2.medium":
    print("this will charge 4 dollors")
elif type == "t2.xlarge":
    print("this will change 8 dollars")
else:
    print("invalid instance type")