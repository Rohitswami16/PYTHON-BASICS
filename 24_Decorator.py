
# Program 1: Adding "Bye" After a Function Call Using a Decorator
def fun(func):
    # Inner function to wrap additional behavior
    def saybye():
        func()  # Call the original function
        print("bye")  # Add additional functionality
    return saybye

@fun  # Decorates the `say_hello` function
def say_hello():
    print("hello")

# Call the decorated function
say_hello()

# Expected Output:
# hello
# bye

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 2: Announcing a Surprise Test Using a Decorator
def take_test(func):
    # Inner function to add surprise announcement
    def online_test():
        print("Surprise test for you!")  # Additional functionality
        func()  # Call the original function
    return online_test

@take_test  # Decorates the `take_class` function
def take_class():
    print("class is going on")

# Call the decorated function
take_class()

# Expected Output:
# Surprise test for you!
# class is going on

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 3: Authentication Using a Decorator
def auth_decorator(func):
    # Inner function to handle authentication logic
    def wrapped():
        user = "viv"
        password = "555"  # Hardcoded credentials for demonstration

        if user == "viv" and password == "555":  # Authentication check
            print("Authentication successful.")  # Success message
            func()  # Call the original function
        else:
            print("Authentication failed.")  # Failure message
    return wrapped

@auth_decorator  # Decorates the `say_hello` function
def say_hello():
    print("Hello, authenticated user!")

# Call the decorated function
say_hello()

# Expected Output:
# Authentication successful.
# Hello, authenticated user!

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
