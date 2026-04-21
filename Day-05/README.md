📌 What are Command Line Arguments?
Command line arguments are values you pass to a Python script when you run it from the terminal.
They let you send input to your program without hardcoding it.

👉 Example:

# python script.py Pranavi 25

Pranavi and 25 are command line arguments

📌 How Python receives them (sys.argv)
Python stores all command line arguments in a list called sys.argv
You need to import the sys module

# import sys

📌 Structure of sys.argv

# import sys
# print(sys.argv)

👉 If you run:

# python script.py hello 123

👉 Output:

# ['script.py', 'hello', '123']

- sys.argv[0] → script name (script.py)
- sys.argv[1] → first argument (hello)
- sys.argv[2] → second argument (123)

📌 Example program

import sys
name = sys.argv[1]
age = sys.argv[2]
print("Name:", name)
print("Age:", age)

📌 Important notes
- All values in sys.argv are strings
- Convert if needed:
# age = int(sys.argv[2])

If you don’t pass enough arguments → you’ll get an IndexError
📌 One-line definition

👉 Command line arguments are inputs passed to a program at runtime via the terminal, accessed in Python using sys.argv.








📌 Environment Variables (env variables)
Environment variables are key–value pairs stored in the system.
Used to store configuration data (like API keys, paths, secrets).
Accessible by programs at runtime.

in the terminal run:
export password="pranavi"

syntax:

import os (to read env variables you have "import os" module)
print(os.getenv("passoword")) (use the function called "os")

when you execute the program in the terminal you should see the password