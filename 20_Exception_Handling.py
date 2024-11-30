
# Program 1: Basic Division Function (Without Exception Handling)
# This program performs division of two numbers without handling any exceptions.
# If a division by zero occurs, the program will terminate with an error.

def division(a, b):
    print("About to start calculation")
    res = a / b
    print(f"Result = {res}")

print("Program is starting")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
division(n1, n2)
print("Program is ending")

# --- Heading: No Exception Handling ---
# Expected Output:
# - If n2 != 0, it calculates and displays the result.
# - If n2 == 0, it raises a ZeroDivisionError and terminates the program.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 2: Division with Exception Handling
# This program performs division of two numbers with exception handling for division by zero.
# If an invalid division (like division by zero) occurs, it gracefully handles the error and displays a message.

def div(a, b):
    print("About to start calculation")
    try:
        res = a / b
        print(f"Result = {res}")
    except ZeroDivisionError:  # Handles division by zero
        print("Division by zero is not allowed")

print("Program is starting")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
div(n1, n2)
print("Program is ending")

# --- Heading: Exception Handling for Division by Zero ---
# Expected Output:
# - If n2 != 0, it calculates and displays the result.
# - If n2 == 0, it catches the ZeroDivisionError and prints "Division by zero is not allowed."

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 3: Division with Detailed Exception Handling
# This program performs division with exception handling, and it also ensures the program executes
# specific actions (like printing "Program about to exit") using a `finally` block.
# It distinguishes between successful and failed division operations using `try`, `except`, and `else`.

def calculation(a, b):
    print("About to start calculation")
    try:
        res = a / b
    except ZeroDivisionError:  # Handles division by zero
        print("Division by zero is not allowed")
    else:  # Executes only if no exception occurs
        print(f"Result = {res}")
    finally:  # Executes regardless of whether an exception occurs
        print("Program about to exit")

print("Program is starting")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
calculation(n1, n2)
print("Program is ending")

# --- Heading: Exception Handling with Finally Block ---
# Expected Output:
# - If n2 != 0, it calculates and displays the result and exits gracefully.
# - If n2 == 0, it catches the ZeroDivisionError, displays an error message, and ensures the program exits cleanly.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 4: Calculation with Multiple Exception Handling
# This program performs division and addition with detailed exception handling.
# It ensures the program executes specific actions (like printing "Program about to exit") using a `finally` block.
# It distinguishes between successful and failed operations using `try`, `except`, and `else`.

def calc(a, b):
    print("About to start calculation")
    try:
        # Attempt division
        div = a / b
        print(f"Division = {div}")
        
        # Attempt addition (uses undefined variable 'c' to trigger NameError)
        add = a + c  # 'c' is undefined
        print(f"Addition = {add}")
    except ZeroDivisionError:  # Handles division by zero
        print("Division by zero is not allowed")
    except NameError:  # Handles undefined variables
        print("Variable not defined")
    else:  # Executes only if no exception occurs
        print("Both operations were successful!")
    finally:  # Executes regardless of whether an exception occurs
        print("Program about to exit")

print("Program is starting")
try:
    # Take user input for two numbers
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    
    # Call the calc function
    calc(n1, n2)
except ValueError:  # Handles non-integer inputs
    print("Error: Please enter valid integers.")
finally:
    print("Program is ending")

# --- Heading: Detailed Exception Handling with Finally Block ---
# Expected Output:
# - If n2 != 0 and all variables are defined, it performs the calculations and exits gracefully.
# - If n2 == 0, it catches the ZeroDivisionError, displays an error message, and exits cleanly.
# - If an undefined variable is used (like 'c'), it catches the NameError and exits cleanly.
# - If invalid input is entered, it handles the ValueError and ends the program.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 5: Age Validation with Custom Exception
# This program checks if the user's age is eligible for voting (age >= 18).
# If the age is less than 18, it raises a `ValueError` with a custom error message.

def validate(age):
    if age >= 18:
        print("Eligible for voting!")
    else:
        raise ValueError("Age must be >= 18")

age = int(input("Enter age: "))
validate(age)

# --- Heading: Custom Exception Handling for Age Validation ---
# Expected Output:
# - If age >= 18, it prints "Eligible for voting!".
# - If age < 18, it raises a ValueError with the message "Age must be >= 18."

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 6: Custom Exception Handling for Age Validation
# This program defines a custom exception `AgeError` to handle age-related errors.
# It validates the user's age for voting eligibility using a `validate` function.
# The program gracefully handles valid, invalid, and non-integer inputs.

# Custom exception for age-related errors
class AgeError(Exception):
    pass

# Function to validate the age for voting eligibility
def validate(age):
    if age >= 18:
        print("Eligible for voting!")
    else:
        # Raise AgeError if age is less than 18
        raise AgeError("Age must be >= 18")

# Main Program
# This block takes user input and handles various scenarios using try-except blocks
try:
    age = int(input("Enter your age: "))  # Prompt the user for their age
    validate(age)  # Call the validate function to check eligibility
except AgeError as e:
    # Handle the custom AgeError exception
    print(f"Error: {e}")
except ValueError:
    # Handle invalid input (e.g., non-integer)
    print("Error: Please enter a valid integer for age.")

# --- Heading: Expected Outputs for Different Scenarios ---
# Case 1: Valid Age (Eligible for Voting)
# Input:
# Enter your age: 20
# Output:
# Eligible for voting!

# Case 2: Invalid Age (Not Eligible for Voting)
# Input:
# Enter your age: 16
# Output:
# Error: Age must be >= 18

# Case 3: Non-Integer Input (Invalid Input)
# Input:
# Enter your age: abc
# Output:
# Error: Please enter a valid integer for age.
