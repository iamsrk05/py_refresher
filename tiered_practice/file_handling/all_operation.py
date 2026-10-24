# ============================================================
# Write mode ("w")
# Opens a file for writing. It creates the file or replaces its contents.
# ============================================================
# file = open("tiered_practice/file_handling/student.txt", "w")

# file.write("I am going to achieve everything.")

# file.close()

file = open("tiered_practice/file_handling/profile.txt", "w")

file.write("Name: Sam\n")
file.write("Course: Data Science\n")
file.write("Language: Python")

file.close()


# ============================================================
# Append mode ("a")
# Adds text to the end of a file without replacing its contents.
# ============================================================
file = open("tiered_practice/file_handling/profile.txt", "a")

file.write("\nGoal: Data Scientist")

file.close()

# ============================================================
# Reading with read()
# Read mode ("r") opens a file for reading; read() returns one string.
# ============================================================
# file = open("tiered_practice/file_handling/profile.txt", "r")

# content = file.read()

# print(content)

with open("tiered_practice/file_handling/profile.txt", "r") as file:
    content = file.read()

print(content)

# ============================================================
# Reading with readlines()
# readlines() returns a list of strings, one for each line.
# ============================================================
with open("tiered_practice/file_handling/profile.txt", "r") as file:
    lines = file.readlines()

print(lines)

# ============================================================
# Reading with readline()
# readline() returns the next line as a string on each call.
# ============================================================
print("Readline Module: ")


with open("tiered_practice/file_handling/profile.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()

print(f"First line: {first_line}")
print(f"Second line: {second_line}")


# ============================================================
# Using with open()
# The with block closes the file automatically when the block ends.
# This example reads all lines again using readlines().
# ============================================================
with open("tiered_practice/file_handling/profile.txt", "r") as file:
    lines = file.readlines()
print(lines)


# ============================================================
# Writing multiple lines with writelines()
# writelines() writes multiple strings from an iterable.
# It does NOT add newline characters automatically.
# ============================================================

skills = [
    "Python\n",
    "SQL\n",
    "Pandas\n",
    "NumPy\n"
]

with open("tiered_practice/file_handling/skills.txt", "w") as file:
    file.writelines(skills)

with open("tiered_practice/file_handling/skills.txt", "r") as file:
    content = file.read()

print(content)


# ============================================================
# Create mode ("x")
# Creates a new file only if it does not already exist.
# ============================================================

import os

x_file = "tiered_practice/file_handling/created_with_x.txt"

if not os.path.exists(x_file):
    with open(x_file, "x") as file:
        file.write("This file was created using x mode.")
    print("New file created")
else:
    print("File already exists, so x mode was not used")
    
    
    
    
# ============================================================
# Deleting a file with os.remove()
# Check first so the program does not crash if the file is missing.
# ============================================================

delete_file = "tiered_practice/file_handling/created_with_x.txt"

if os.path.exists(delete_file):
    os.remove(delete_file)
    print("File deleted")
else:
    print("File does not exist")