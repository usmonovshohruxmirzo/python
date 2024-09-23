# 1 Python Strings

print("Hello")
print('Hello')

a = "JS is the best"
print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes ("""):
b = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
s = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(b)
print(s)

# Strings are Arrays
d = "Docker"
print(d[0])

# Looping Through a String
for x in "JAVASCRIPT":
    print(x)

# String Length
l = "hello"
print(len(a))

# Check String "in"
txt = "The best things in life are free!"
print("free" in txt)
print("not free" in txt)

if "free" in txt:
    print("Yes, 'free' is present")

# Check if NOT "not in"
print("expensive" not in txt)


# 2 Slicing Strings
slcStr = "python"
print(slcStr[2:5])

# Slice From the Start
print(slcStr[:5])

# Slice To the End
print(slcStr[2:])

# Negative Indexing
print(slcStr[-5:-2])


# 3 Modify Strings
# Upper Case
modifyStr = " Hello World "
print(modifyStr.upper())

# Lower Case
print(modifyStr.lower())

# Remove Whitespace
print(modifyStr.strip())

# Replace String
print(modifyStr.replace("d","D"))

# Split String
print(modifyStr.split(" "))


# 4 String Concatenation
aStr = "Hello"
bStr = "World"
cStr = aStr + " " + bStr
print(cStr)

# 5 String Format
# F-Strings

age = 36
ftxt = f"My name is Alex, I am {age}"
print(ftxt)

price = 50000
ftxt2 = f"Laptop price is {price:.2f}, RAM: {8 * 8}"
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
print(ftxt2)


# 6 Escape Character

# \' 	Single Quote 	
# \\ 	Backslash 	
# \n 	New Line 	
# \r 	Carriage Return 	
# \t 	Tab 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value

txtEC = "We are the so-called \"Vikings\" from the north."
print(txtEC)

# 7 String Methods
strMethods = "\tSTRING methodss"


print(strMethods.capitalize()) # Converts the first character to upper case

print(strMethods.casefold()) # Converts string into lower case

print(strMethods.center(30, "+")) # Returns a centered string (length, character)

print(strMethods.count("s")) # Returns the number of times a specified value occurs in a string

print(strMethods.encode()) # Returns an encoded version of the string

print(strMethods.endswith("ss")) # Returns true if the string ends with the specified value

print(strMethods.expandtabs(2)) # Sets the tab size of the string

print(strMethods.find("methodss")) # Searches the string for a specified value and returns the position of where it was found

print("My name is {fname}, I'm {age}".format(fname="Alex", age=50)) # Formats specified values in a string

print("{x} {y}".format_map({"x": 5, "y": 10})) # Formats specified values in a string

print(strMethods.index("S")) # Searches the string for a specified value and returns the position of where it was found

print("Company12".isalnum()) # Returns True if all characters in the string are alphanumeric

print("abc".isalpha()) # Returns True if all characters in the string are in the alphabet

print("abc".isascii()) # Returns True if all characters in the string are ascii characters

print("123".isdecimal()) #	Returns True if all characters in the string are decimals

print("123".isdigit(), "\u00B2".isdigit()) # Returns True if all characters in the string are digits

print("strMethods".isidentifier()) # Returns True if the string is an identifier. A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

print("abc".islower()) # Returns True if all characters in the string are lower case

print("123".isnumeric()) # Returns True if all characters in the string are numeric

print("isprintable".isprintable()) # Returns True if all characters in the string are printable

print(" ".isspace()) # Returns True if all characters in the string are upper case

print("hello".istitle()) # Returns True if the string follows the rules of a title

print("HELLO".isupper()) # Returns True if all characters in the string are upper case

myTuple = ("John", "Peter", "Vicky")
print(" ".join(myTuple)) # Joins the elements of an iterable to the end of the string

print("html".ljust(20), "css") # Returns a left justified version of the string

print("HELLO".lower()) # Converts a string into lower case

print("        Hello        ".lstrip()) # Returns a left trim version of the string

mytable = "Hello".maketrans("H", "F")
print("Hello".translate(mytable))

print("I could eat bananas all day".partition("bananas"))

print("JS is the best".replace("JS","TS")) # Returns a string where a specified value is replaced with a specified value

print("Mi casa, su casa.".rfind("casa")) # Searches the string for a specified value and returns the last position of where it was found

print("Mi casa, su casa.".rindex("casa")) # Searches the string for a specified value and returns the last position of where it was found

print("hello".rjust(20)) # Returns a right justified version of the string

print("I could eat bananas all day, bananas are my favorite fruit".rpartition("bananas"))

print("apple, banana, cherry".rsplit(",")) # Splits the string at the specified separator, and returns a list

print("apple, banana, cherry".split(",")) # Splits the string at the specified separator, and returns a list

print("Thank you for the music\nWelcome to the jungle".splitlines()) # 	Splits the string at line breaks and returns a list

print("hello".startswith("he")) # Returns true if the string starts with the specified value

print("       hello       ".strip()) # 	Returns a trimmed version of the string

print("hello".swapcase()) # Swaps cases, lower case becomes upper case and vice versa

print("hello".title()) # Converts the first character of each word to upper case

print("Hello Sam!".translate({83: 80}))

print("hello".upper()) # Converts a string into upper case

print("50".zfill(10)) # Fills the string with a specified number of 0 values at the beginning