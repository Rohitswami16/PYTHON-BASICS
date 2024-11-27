
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

# Program 4: Age Validation with Custom Exception
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
