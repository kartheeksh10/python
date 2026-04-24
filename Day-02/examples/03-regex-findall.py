import re

# UNDERSTANDING RAW STRINGS (r"")
print("=== WHAT DOES 'r' MEAN BEFORE STRINGS? ===\n")

# The 'r' creates a RAW STRING - it treats backslashes literally
# This is very important for regex patterns!

# Example: Regular string vs Raw string
print("Regular string:")
regular_string = "Hello\nWorld"  # \n is interpreted as newline
print(f"'{regular_string}'")
print()

print("Raw string:")
raw_string = r"Hello\nWorld"  # \n is treated as literal characters
print(f"'{raw_string}'")
print()

# Why is this important for regex?
print("=== WHY RAW STRINGS ARE IMPORTANT FOR REGEX ===\n")

# Example 1: Finding backslashes in text
text_with_backslash = "File path: C:\\Users\\John\\Documents"
print(f"Text: {text_with_backslash}")

# Without raw string - CONFUSING!
pattern_normal = "\\\\Users"  # Need 4 backslashes to match 2!
matches_normal = re.findall(pattern_normal, text_with_backslash)
print(f"Normal string pattern: '{pattern_normal}'")
print(f"Matches: {matches_normal}")

# With raw string - CLEAR!
pattern_raw = r"\\Users"  # Only need 2 backslashes
matches_raw = re.findall(pattern_raw, text_with_backslash)
print(f"Raw string pattern: '{pattern_raw}'")
print(f"Matches: {matches_raw}")
print()

# Example 2: Digit patterns
print("=== DIGIT PATTERNS EXAMPLE ===")
text_digits = "I have 25 apples and 100 oranges"
print(f"Text: {text_digits}")

# Both work the same for simple patterns like \d
pattern_normal_digit = "\\d+"  # Need to escape the backslash
pattern_raw_digit = r"\d+"     # Raw string - cleaner and more readable

matches_normal_digit = re.findall(pattern_normal_digit, text_digits)
matches_raw_digit = re.findall(pattern_raw_digit, text_digits)

print(f"Normal string: '{pattern_normal_digit}' -> {matches_normal_digit}")
print(f"Raw string: '{pattern_raw_digit}' -> {matches_raw_digit}")
print()

print("=== KEY POINTS ABOUT RAW STRINGS ===")
print("1. Raw strings treat backslashes (\\) as literal characters")
print("2. Regular strings interpret backslashes as escape characters")
print("3. Raw strings make regex patterns much more readable")
print("4. Always use raw strings for regex patterns: r'pattern'")
print("5. Examples of escape characters in regular strings:")
print("   \\n = newline")
print("   \\t = tab")
print("   \\' = single quote")
print("   \\\\ = literal backslash")
print()

# BEGINNER REGEX EXAMPLES - Step by Step Learning

print("=== BASIC REGEX PATTERNS ===\n")

# Example 1: Finding simple words
text1 = "I love Python programming and Python is easy"
pattern1 = r"Python"  # Just finds the exact word "Python"
matches1 = re.findall(pattern1, text1)
print(f"Text: {text1}")
print(f"Pattern: {pattern1}")
print(f"Matches: {matches1}")
print()

# Example 2: Finding digits
text2 = "I have 5 apples and 10 oranges"
pattern2 = r"\d"  # \d means any digit (0-9)
matches2 = re.findall(pattern2, text2)
print(f"Text: {text2}")
print(f"Pattern: {pattern2} (\\d means any digit)")
print(f"Matches: {matches2}")
print()

# Example 3: Finding multiple digits together
text3 = "I have 25 apples and 100 oranges"
pattern3 = r"\d+"  # \d+ means one or more digits together
matches3 = re.findall(pattern3, text3)
print(f"Text: {text3}")
print(f"Pattern: {pattern3} (\\d+ means one or more digits)")
print(f"Matches: {matches3}")
print()

# Example 4: Finding words (letters only)
text4 = "Hello123 World456 Python"
pattern4 = r"[a-zA-Z]+"  # [a-zA-Z]+ means one or more letters
matches4 = re.findall(pattern4, text4)
print(f"Text: {text4}")
print(f"Pattern: {pattern4} (letters only)")
print(f"Matches: {matches4}")
print()

# Example 5: Finding words that start with capital letter
text5 = "Python is Great for Data Science"
pattern5 = r"[A-Z][a-z]+"  # [A-Z] = capital letter, [a-z]+ = lowercase letters
matches5 = re.findall(pattern5, text5)
print(f"Text: {text5}")
print(f"Pattern: {pattern5} (capital letter + lowercase letters)")
print(f"Matches: {matches5}")
print()

# Example 6: Finding email pattern (simplified)
text6 = "Contact me at john@gmail.com or mary@yahoo.com"
pattern6 = r"\w+@\w+\.\w+"  # \w+ = word characters, @ = literal @, \. = literal dot
matches6 = re.findall(pattern6, text6)
print(f"Text: {text6}")
print(f"Pattern: {pattern6} (word@word.word)")
print(f"Matches: {matches6}")
print()

# Example 7: Finding phone numbers (simple pattern)
text7 = "Call me at 123-456-7890 or 555-123-4567"
pattern7 = r"\d{3}-\d{3}-\d{4}"  # \d{3} = exactly 3 digits
matches7 = re.findall(pattern7, text7)
print(f"Text: {text7}")
print(f"Pattern: {pattern7} (3digits-3digits-4digits)")
print(f"Matches: {matches7}")
print()

print("=== REGEX CHEAT SHEET ===")
print("\\d    = any digit (0-9)")
print("\\w    = any word character (letters, digits, underscore)")
print("\\s    = any whitespace (space, tab, newline)")
print("+     = one or more of the previous character")
print("*     = zero or more of the previous character")
print("?     = zero or one of the previous character")
print("{3}   = exactly 3 of the previous character")
print("[a-z] = any lowercase letter")
print("[A-Z] = any uppercase letter")
print("[0-9] = any digit (same as \\d)")
print(".     = any character except newline")
print("^     = start of string")
print("$     = end of string")
