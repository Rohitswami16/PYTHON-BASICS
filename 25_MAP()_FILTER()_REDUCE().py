# Program 1: Using `map` to Apply a Function
lst = [5, 10, 15, 20, 25]

def sq(num):
    return num * num  # Function to return the square of a number

# Apply the `sq` function to each item in the list using `map`
sql = list(map(sq, lst))
print(sql)

# Expected Output:
# [25, 100, 225, 400, 625]

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 2: Using `map` with a Lambda Function
lst = [5, 10, 15, 20, 25]

# Apply a lambda function to square each number in the list
sql = list(map(lambda num: num * num, lst))
print(sql)

# Expected Output:
# [25, 100, 225, 400, 625]

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 3: Using `filter` to Filter Even Numbers
lst = [5, 10, 15, 20, 25]

def even(num):
    # Function to check if a number is even
    return num % 2 == 0

# Filter the list to keep only even numbers using `filter`
elist = list(filter(even, lst))
print(elist)

# Expected Output:
# [10, 20]

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 4: Using `filter` with a Lambda Function
lst = [5, 10, 15, 20, 25]

# Use a lambda function to filter even numbers
elist = list(filter(lambda num: num % 2 == 0, lst))
print(elist)

# Expected Output:
# [10, 20]

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 5: Using `reduce` to Accumulate a Result (Sum)
from functools import reduce

lst = [5, 10, 15, 20, 25]

def add(a, b):
    # Function to add two numbers
    return a + b

# Use `reduce` to accumulate the sum of all the numbers in the list
sum = reduce(add, lst)
print(sum)

# Expected Output:
# 75

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 6: Using `reduce` with a Lambda Function
from functools import reduce

lst = [5, 10, 15, 20, 25]

# Use `reduce` with a lambda to accumulate the sum of all numbers
sum = reduce(lambda a, b: a + b, lst)
print(sum)

# Expected Output:
# 75
