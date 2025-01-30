# Program 1: Reading the Entire File

file = open('demo.txt', 'r')  # Open the file in read mode
text = file.read()  # Read the entire content of the file
print(text)  # Print the content
file.close()  # Close the file

# Expected Behavior:
# Prints the entire content of `demo.txt`.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 2: Reading a Single Line

file = open('demo.txt', 'r')  # Open the file in read mode
text = file.readline()  # Read the first line of the file
print(text)  # Print the line
file.close()  # Close the file

# Expected Behavior:
# Prints the first line of `demo.txt`.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 3: Reading All Lines as a List

file = open('demo.txt', 'r')  # Open the file in read mode
text = file.readlines()  # Read all lines into a list
print(text)  # Print the list of lines
file.close()  # Close the file

# Expected Behavior:
# Prints all lines of `demo.txt` as a list.
# Example: ['Line 1\n', 'Line 2\n', ...]

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 4: Writing to a File (Overwrite Mode)

file = open('demo.txt', 'w')  # Open the file in write mode
file.write("hello python")  # Write content to the file
file.close()  # Close the file

# Expected Behavior:
# Overwrites `demo.txt` with the text: "hello python".
# Existing content in the file will be deleted.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 5: Writing to a New File

file2 = open('demo2.txt', 'w')  # Open (or create) `demo2.txt` in write mode
file2.write("hello python new one")  # Write content to the file
file2.close()  # Close the file

# Expected Behavior:
# Creates a new file `demo2.txt` (if not already present) and writes the text "hello python new one".

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 6: Appending to a File

file = open('demo.txt', 'a')  # Open the file in append mode
file.write("\nhello from python")  # Append new content with a newline
file.close()  # Close the file

# Expected Behavior:
# Appends the text "\nhello from python" to the end of `demo.txt` without removing existing content.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Key Points:
# File Modes:

# 'r': Read mode (default, errors if the file doesn't exist).
# 'w': Write mode (creates a file if it doesn’t exist, overwrites if it does).
# 'a': Append mode (adds content to the end without overwriting).
# File Handling:

# Always close files after opening them (file.close()), or use a context manager (with open(...)).
