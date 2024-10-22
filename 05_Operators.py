''' 
Arithmetic Operators: Perform basic mathematical operations (+, -, *, /, %, **, //).
Comparison Operators: Compare values and return True or False.
Logical Operators: Combine multiple conditions using and, or, and not.
Assignment Operators: Modify variables using +=, -=, *=, /=, and %=. '''

# Initializing variables
a = 10
b = 5
c = 5

# Arithmetic operations
print(a + b)  # Addition: 10 + 5 = 15
print(a - b)  # Subtraction: 10 - 5 = 5
print(a * b)  # Multiplication: 10 * 5 = 50
print(a / b)  # Division: 10 / 5 = 2.0 (result is a float)
print(a % b)  # Modulus: 10 % 5 = 0 (remainder of the division)
print(a ** b)  # Exponentiation: 10 raised to the power of 5 = 100000
print(a // b)  # Floor division: 10 // 5 = 2 (integer division)

print()  # Adding a blank line for readability

# Comparison operations (returns True or False)
print(a < b)   # Less than: 10 < 5 = False
print(a > b)   # Greater than: 10 > 5 = True
print(a <= b)  # Less than or equal to: 10 <= 5 = False
print(a >= b)  # Greater than or equal to: 10 >= 5 = True
print(b == c)  # Equal to: 5 == 5 = True (because b and c are both 5)
print(a != b)  # Not equal to: 10 != 5 = True

print()  # Adding a blank line for readability

# Logical operations
print(True or True)    # True (either condition is True)
print(True or False)   # True (either condition is True)
print(False or True)   # True (either condition is True)
print(False or False)  # False (both conditions are False)

print()  # Adding a blank line for readability

print(True and True)   # True (both conditions are True)
print(True and False)  # False (both conditions are not True)
print(False and True)  # False (both conditions are not True)
print(False and False) # False (both conditions are False)

print()  # Adding a blank line for readability

print(not(True))   # False (negates True)
print(not(False))  # True (negates False)

print()  # Adding a blank line for readability

# Assignment operations
a = 10  # Assigning the value 10 to a
print(a)  # Output: 10

a += 5  # Equivalent to a = a + 5 (a becomes 15)
print(a)  # Output: 15

a -= 5  # Equivalent to a = a - 5 (a becomes 10 again)
print(a)  # Output: 10

a *= 5  # Equivalent to a = a * 5 (a becomes 50)
print(a)  # Output: 50

a /= 5  # Equivalent to a = a / 5 (a becomes 10.0)
print(a)  # Output: 10.0

a %= 5  # Equivalent to a = a % 5 (a becomes 0.0, remainder of 10.0 / 5)
print(a)  # Output: 0.0
