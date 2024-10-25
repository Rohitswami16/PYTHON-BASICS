# ------------------------------------------
# Check if the entered number is a palindrome using a string approach

print("Enter a number")  # Prompt the user to enter a number
num = int(input())  # Convert the input to an integer and store it in 'num'
originalnum = num  # Store the original number for comparison later
newnum = ""  # Initialize an empty string to build the reversed number

# Loop to extract each digit from 'num' and build the reversed number as a string
while num > 0:
    ls = num % 10  # Get the last digit of 'num'
    newnum = newnum + str(ls)  # Append the last digit to 'newnum' as a string
    num = num // 10  # Remove the last digit from 'num' by integer division

# Check if the original number and the reversed string are the same
if originalnum == int(newnum):  # Convert 'newnum' back to an integer for comparison
    print("Palindrome")  # Print if the number is a palindrome
else:
    print("Not a palindrome")  # Print if the number is not a palindrome


# ------------------------------------------
# Check if the entered number is a palindrome using a mathematical approach

print("Enter a number")  # Prompt the user to enter a number
num = int(input())  # Convert the input to an integer and store it in 'num'
originalnum = num  # Store the original number for comparison later
newnum = 0  # Initialize 'newnum' as 0 to build the reversed number mathematically

# Loop to extract each digit from 'num' and build the reversed number
while num > 0:
    ls = num % 10  # Get the last digit of 'num'
    newnum = (newnum * 10) + ls  # Append the last digit to 'newnum' by shifting digits left
    num = num // 10  # Remove the last digit from 'num' by integer division

# Check if the original number and the reversed number are the same
if originalnum == newnum:  # Compare 'originalnum' and 'newnum' to see if they match
    print("Palindrome")  # Print if the number is a palindrome
else:
    print("Not a palindrome")  # Print if the number is not a palindrome


# ------------------------------------------
# Print a grid of asterisks using nested loops

# Outer loop to iterate over 4 rows
for i in range(4):
    # Inner loop to print 5 asterisks in each row
    for j in range(5):
        print("*", end="")  # Print an asterisk without a newline
    print()  # Move to the next line after printing 5 asterisks

print()  # Print a blank line for separation between patterns

# ------------------------------------------

# Print a grid of asterisks using string multiplication

# Loop to print 4 rows of asterisks
for i in range(4):
    print("*" * 5)  # Print 5 asterisks in each row using string multiplication
