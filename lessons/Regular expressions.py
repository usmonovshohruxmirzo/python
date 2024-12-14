import re

# Match a Pattern at the Start of a String:
result = re.match(r"\d+", "123abc")
print("match", result.group())  

# Search for a Pattern Anywhere in a String
result = re.search(r"\d+", "abc1234abc")
print("search", result.group())

# Find All Matches:
result = re.findall(r"\d+", "1abc1abc2")
print("findall", result)

# Replace Patterns with Another String:
result = re.sub(r"\d+", "#", "1abc1abc2")
print("sub", result)

# Split a String by a Pattern
result = re.split(r"\d+", "a1b2c3")
print("split" ,result)

# Iterate Over All Matches
result = re.finditer(r"\d+", "a1b2c3")
for match in result:
    print(match.group())