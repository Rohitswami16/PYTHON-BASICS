# First pattern: Right-angled triangle of stars
for i in range(6):
    # Inner loop prints '*' i times for each row
    for j in range(i):
        print("*", end=' ')
    # Move to the next line after each row
    print()

# Expected output:

# *
# * *
# * * *
# * * * *
# * * * * *

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Second pattern: Hollow square of stars
for i in range(5):
    for j in range(5):
        # Print '*' for the border cells (first and last row/column)
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=' ')
        else:
            # Print a space for inner cells to create a hollow effect
            print(" ", end=' ')
    # Move to the next line after each row
    print()

# Expected output:

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Third pattern: Inverted triangle with numbers
for i in range(4, 0, -1):  # Loop from 4 down to 1
    # Inner loop prints the current value of i, i times
    for j in range(i):
        print(i, end=' ')
    # Move to the next line after each row
    print()

# Expected output:

# 4 4 4 4
# 3 3 3
# 2 2
# 1

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Loop to determine the number of rows in the triangle
for i in range(1, 6):
    # Inner loop to print spaces for alignment, decreasing each row
    for j in range(1, 6 - i):
        print("_", end="")  # Print underscores to shift the 'x' characters to the right

    # Inner loop to print 'x' characters, increasing each row
    for k in range(1, i + 1):
        print("x", end="")  # Print 'x' without newline to build the row

    # Move to the next line after completing each row
    print()

# Expected output:
____x
___xx
__xxx
_xxxx
xxxxx

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

# Take the number of columns as input from the user
columns = int(input("Enter the number of columns: "))

# Outer loop for iterating through each row
for i in range(rows):
    # Inner loop for iterating through each column in the current row
    for j in range(columns):
        # Print '*' without newline to create a continuous row of stars
        print('*', end='')
    # After finishing a row, print a newline to start the next row
    print()

# Expected output:
*****
*****
*****
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

for i in range(1, 6):               # Outer loop for each row, iterating from 1 to 5.
    for j in range(1, 6 - i):       # Inner loop to print leading dashes, based on the current row number.
        print(" ", end='')          # Print '-' without a newline to create the correct alignment.
    
    x = 1                           # Initialize x to 1, representing the start of the number sequence.
    
    for k in range(1, (2 * i)):     # Inner loop to print numbers, with range (2*i) creating a pyramid effect.
        print(k, end='')            # Print the current value of k without newline, forming the increasing and decreasing pattern.
        
        if k < i:                   # If we haven't reached the middle of the pyramid row, increase x.
            x = x + 1               # Increment x for the ascending part of the row.
        else:                       # After reaching the middle, start the descending pattern.
            x = x - 1               # Decrement x for the descending part of the row.
    
    print()                         # Move to the next line after completing the current row.

# Expected output:

    1
   123
  12345
 1234567
123456789
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
