# Program 1: Iterating Over a List
lst = [11, 22, 33, 44, 55]
for i in lst:
    print(i)

# Expected Output:
# 11
# 22
# 33
# 44
# 55

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 2: Iterating Over Digits of an Integer
num = 12345

# Fix: Convert the integer to a string for iteration
for i in str(num):       
    print(i)

# Expected Output:
# 1
# 2
# 3
# 4
# 5

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 3: Using an Iterator Over a List
ls = [11, 22, 33, 44, 55]
itr = iter(ls)  # Create an iterator for the list

for i in ls:
    print(next(itr))

# Expected Output:
# 11
# 22
# 33
# 44
# 55

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Program 4: Iterating Using Range and an Iterator
nums = [11, 22, 33, 44, 55]
itr = iter(nums)  # Create an iterator for the list

for i in range(len(nums)):
    print(next(itr))

# Expected Output:
# 11
# 22
# 33
# 44
# 55

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

  # Program 5: Defining a Circle Class and Creating Objects
class Circle:
    def __init__(self, r):
        self.r = r  # Store the radius as an instance variable

# Create objects of the Circle class with different radii
c1 = Circle(10)
c2 = Circle(20)
c3 = Circle(30)
c4 = Circle(40)
c5 = Circle(50)

# Access and print the radius of each circle
print(c1.r)  # Expected Output: 10
print(c2.r)  # Expected Output: 20
print(c3.r)  # Expected Output: 30
print(c4.r)  # Expected Output: 40
print(c5.r)  # Expected Output: 50
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
