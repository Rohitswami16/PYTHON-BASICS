# String concatenation example
s1 = "hello"  # String variable s1
s2 = s1 + ("World")  # Concatenating "World" to s1 and storing in s2

print(s1)  # Output: hello (original string)
print(s2)  # Output: helloWorld (concatenated string)

# String comparison and memory address check
s3 = "Python"  # String variable s3
s4 = "Python"  # String variable s4

# `is` checks if both variables point to the same object in memory (not just value equality)
print(s3 is s4)  # Output: True (both refer to the same memory location for the same string)

# Print the memory address of s3 and s4
print(id(s3))  # Memory address of s3
print(id(s4))  # Memory address of s4 (same as s3 because Python optimizes identical strings by reusing the same memory)

# Taking integer input from the user and performing addition
# num1 and num2 are taken as input from the user
num1 = int(input("Enter num 1: "))  # Converts input string to an integer
num2 = int(input("Enter num 2: "))  # Converts input string to an integer

# Printing the sum of num1 and num2
print(num1 + num2)  # Output will be the sum of the two input integers
