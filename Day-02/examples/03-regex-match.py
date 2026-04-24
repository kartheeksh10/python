import re

# REGEX MATCH EXAMPLES - Beginner Friendly

print("=== UNDERSTANDING re.match() ===")
print("re.match() only matches at the BEGINNING of the string\n")

# Example 1: Basic match - Success case
text1 = "Python is awesome"
pattern1 = r"Python"
match1 = re.match(pattern1, text1)
print(f"Text: '{text1}'")
print(f"Pattern: '{pattern1}'")
if match1:
    print(f"Match found: '{match1.group()}'")
    print(f"Match position: {match1.start()}-{match1.end()}")
else:
    print("No match")
print()

# Example 2: Basic match - Failure case
text2 = "I love Python programming"
pattern2 = r"Python"
match2 = re.match(pattern2, text2)
print(f"Text: '{text2}'")
print(f"Pattern: '{pattern2}'")
if match2:
    print(f"Match found: '{match2.group()}'")
else:
    print("No match (Python is not at the beginning)")
print()

# Example 3: Matching numbers at the start
text3 = "123 Main Street"
pattern3 = r"\d+"  # \d+ means one or more digits
match3 = re.match(pattern3, text3)
print(f"Text: '{text3}'")
print(f"Pattern: '{pattern3}' (one or more digits)")
if match3:
    print(f"Match found: '{match3.group()}'")
else:
    print("No match")
print()

# Example 4: Matching email format from start
text4 = "john@example.com sent you a message"
pattern4 = r"\w+@\w+\.\w+"  # simple email pattern
match4 = re.match(pattern4, text4)
print(f"Text: '{text4}'")
print(f"Pattern: '{pattern4}' (email format)")
if match4:
    print(f"Match found: '{match4.group()}'")
else:
    print("No match")
print()

# Example 5: Matching phone number at start
text5 = "123-456-7890 is my phone number"
pattern5 = r"\d{3}-\d{3}-\d{4}"  # phone number format
match5 = re.match(pattern5, text5)
print(f"Text: '{text5}'")
print(f"Pattern: '{pattern5}' (phone format)")
if match5:
    print(f"Match found: '{match5.group()}'")
else:
    print("No match")
print()

# Example 6: Case sensitivity
text6 = "python is great"
pattern6 = r"Python"  # Capital P
match6 = re.match(pattern6, text6)
print(f"Text: '{text6}'")
print(f"Pattern: '{pattern6}' (case sensitive)")
if match6:
    print(f"Match found: '{match6.group()}'")
else:
    print("No match (case sensitive - 'python' != 'Python')")
print()

# Example 7: Case insensitive matching
text7 = "python is great"
pattern7 = r"Python"
match7 = re.match(pattern7, text7, re.IGNORECASE)  # Case insensitive flag
print(f"Text: '{text7}'")
print(f"Pattern: '{pattern7}' (case insensitive)")
if match7:
    print(f"Match found: '{match7.group()}'")
else:
    print("No match")
print()

print("=== COMPARISON: match() vs search() vs findall() ===")
test_text = "Hello Python world, Python is amazing"
test_pattern = r"Python"

print(f"Text: '{test_text}'")
print(f"Pattern: '{test_pattern}'")

# Using match()
match_result = re.match(test_pattern, test_text)
print(f"re.match(): {match_result.group() if match_result else 'No match'}")

# Using search()
search_result = re.search(test_pattern, test_text)
print(f"re.search(): {search_result.group() if search_result else 'No match'}")

# Using findall()
findall_result = re.findall(test_pattern, test_text)
print(f"re.findall(): {findall_result}")

print("\n=== KEY POINTS ===")
print("1. re.match() only matches at the START of the string")
print("2. re.search() finds the FIRST occurrence anywhere in the string")
print("3. re.findall() finds ALL occurrences in the string")
print("4. Use re.IGNORECASE flag for case-insensitive matching")
