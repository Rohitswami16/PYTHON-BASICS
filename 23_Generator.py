# Program 1: Using a Generator Function
def fun():
    # Yields values one at a time
    yield 11
    yield 22
    yield 33
    yield 44
    yield 55

# Creating a generator object
lucky_list = fun()

# Using `next` to retrieve values from the generator
print(next(lucky_list))  # Retrieves the first value: 11
print(next(lucky_list))  # Retrieves the second value: 22
print(next(lucky_list))  # Retrieves the third value: 33

# Expected Output:
# 11
# 22
# 33

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 2: Using a Generator Expression
nums = (num for num in range(1, 11))  # Generator for numbers 1 to 10

# Assigning the generator to a variable
lucky_list = nums

# Using `next` to retrieve values from the generator
print(next(lucky_list))  # Retrieves the first value: 1
print(next(lucky_list))  # Retrieves the second value: 2
print(next(lucky_list))  # Retrieves the third value: 3

# Expected Output:
# 1
# 2
# 3
