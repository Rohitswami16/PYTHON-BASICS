# This function greets the user with a morning message
def greet():
    print("Good Morning")

# Calling the greet function to display the greeting
greet()

# This function prints a series of instructions
def fun():
    print("Instruction 1")
    print("Instruction 2")
    print("Instruction 3")

# Testing the fun function by calling it
print("testing")
fun()

# This function performs addition without parameters and returns no value
def add():
    a = 10  # First number
    b = 20  # Second number
    sum = a + b  # Calculate the sum of a and b
    print("Addition Result:", sum)  # Print the result of addition

# Calling the add function to display the addition result
add()

# This function takes two parameters, subtracts them, and returns the result
def sub(a, b):
    return a - b  # Return the difference between a and b

# Calling the sub function and printing the subtraction result
print("Substraction result:", sub(20, 10))

# This function takes two parameters and prints their multiplication result
def mul(a, b):
    print("Multiplication Result:", a * b)  # Print the result of multiplying a and b

# Calling the mul function to display the multiplication result
mul(10, 20)

# This function performs division without parameters and returns the result
def div():
    a = 10  # Numerator
    b = 5   # Denominator
    return a / b  # Return the result of dividing a by b

# Calling the div function and printing the division result
print("Division Result:", div())
