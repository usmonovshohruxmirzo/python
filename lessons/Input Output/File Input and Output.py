# file = open(filepath, mode, buffering, encoding, errors, newline, closed, opener)

# file = open("test.txt", "r")
# text = file.read()
# text = file.read(5)

# text = file.readline()
# text = file.readlines()
# print(text)

# for word in file:
#     print(word)


# ==== Python File Write

# file = open("test.txt", "a")
# file.write("\nreactjs")
# file.close()

# f = open("test.txt", "r")
# print(f.read())

# file = open("test.txt", "w")
# file.write("\nreactjs")
# file.close()
#
# f = open("test.txt", "r")
# print(f.read())

# Create a New File
# create_file = open("new.txt", "x")
# open_file = open("new.txt", "a")
# open_file.write("new file added \nhtml,css,js")


# Delete a File

# import os
# os.remove("test.txt")
# if os.path.exists("test.txt"):
#     os.remove("test.txt")
#     print("test.txt", "removed")
# else:
#     print("The file does not exist")

# if os.path.exists("test_folder"):
#     os.rmdir("test_folder")
#     print("test_folder", "removed")
# else:
#     print("The Folder does not exist")


# small program
import os
first_name = input("enter your first name: ".capitalize())
last_name = input("enter your last name: ".capitalize())

os.mkdir(f"{first_name} {last_name}")
folder_name = f"{first_name} {last_name}"
file = open(f"{folder_name}/{first_name}_{last_name}.txt", "x")
open_file = open(f"{folder_name}/{first_name}_{last_name}.txt", "a")
open_file.write(f"{first_name} {last_name}")