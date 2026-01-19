# Import the os module to work with the operating system
import os

# Path of the directory whose contents we want to list
# Note: Using a raw string (r"...") so backslashes are not treated as escape characters
path = r"C:\Users\vicky\OneDrive\python_course"

# os.listdir() returns a list of every file and folder in the given directory
contents = os.listdir(path)

# Print the name of the directory
print(f"Contents of '{path}': ")

# Loop through each item in the directory list
for item in contents:
    print(item)