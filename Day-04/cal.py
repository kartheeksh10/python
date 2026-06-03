import sys
import os 

def add(num1, num2):
    c = num1 + num2
    return c

def sub(num1, num2):
    d = num1 - num2
    return d

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]

if operation == "add":
    output = (add(num1, num2))
    print(output)

elif operation == "sub":
    print(sub(num1, num2))

else:
    print("invalid opertion")

passwd=os.getenv("password")
print(passwd)