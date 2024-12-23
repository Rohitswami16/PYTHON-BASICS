# Define a list with integers
ls = [10, 20, 30, 40, 50]

print(ls)  # Print the entire list
print(type(ls))  # Print the type of the list

# Access specific elements in the list
print(ls[0])  # Print the first element
print(ls[3])  # Print the fourth element

print(ls[-1])  # Print the last element using negative indexing
print(ls[-4])  # Print the second element using negative indexing

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Define a list with mixed data types
lst = [10, 2.05, "Thirty", False]

print(lst)  # Print the original list

lst.append(99)  # Append 99 to the end of the list
print(lst)

lst.insert(2, 100)  # Insert 100 at index 2
print(lst)

print(lst.pop())  # Remove and print the last element

lst.remove(10)  # Remove the first occurrence of 10 from the list
print(lst)

del lst[1]  # Delete the element at index 1
print(lst)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Define a list of integers
ls1 = [10, 20, 30, 40, 50, 60]

# Print the square of each element in the list
for i in ls1:
    print(i**2)

# Calculate the sum of all elements in the list
sum = 0
for i in ls1:
    sum += i

print(sum)  # Print the total sum

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Separate even and odd numbers into two lists
ls2 = [10, 20, 23, 35, 30, 40, 50, 75, 60, 99]
list1 = []  # List to store even numbers
list2 = []  # List to store odd numbers

for i in ls2:
    if i % 2 == 0:
        list1.append(i)  # Append even numbers to list1
    else:
        list2.append(i)  # Append odd numbers to list2

# Print the original list and the two new lists
print(f"Original list : {ls2}")
print(f"even list : {list1}")
print(f"odd list : {list2}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create an empty list
ls3 = []

# Get the number of elements from the user
n = int(input("Enter the number of elements: "))

# Loop to get user input for each element
for i in range(1, n):
    # Add each number entered by the user to the list
    ls3.append(int(input(f"Enter the {i} number: ")))

# Print the list of numbers
print(ls3)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------








