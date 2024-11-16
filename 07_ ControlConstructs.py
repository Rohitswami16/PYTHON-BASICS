# ------------------------------------------

# <-------------------------------------------------------------------Control Constructs in Python------------------------------------------------------------>
# CONDITIONAL STATEMENT (if)
# Welcoming the user to college and checking their marks for tech club eligibility
print("Welcome to college")
marks = int(input("Enter the Marks: "))

# Using 'if' to check if marks are greater than 80 to welcome them to the tech club
if marks > 80:
    print("Welcome to tech club")
# ------------------------------------------
# CONDITIONAL STATEMENT (if-else)
# Prompting the user to enter a number to check if it's even or odd
print("Enter a number")
num1 = int(input())

# Using 'if-else' to check if the number is even or odd
if(num1 % 2 == 0):
    print("Even number")
else:
    print("Odd number")

# ------------------------------------------
# CONDITIONAL STATEMENT (if-elif-else)
# Asking the user to enter their marks to assign a gift based on the marks
print("Enter Marks")
marks = int(input())

# Using 'if-elif-else' to decide the gift based on the range of marks
if marks > 90 and marks <= 100:
    print("Laptop")
elif marks > 76 and marks <= 90:
    print("Tablet")
elif marks > 60 and marks <= 75:
    print("Smart Watch")
elif marks > 40 and marks <= 60:
    print("Bicycle")
else:
    # No gift if marks are below 40
    print("Get lost")

# ------------------------------------------

# Asking the user to enter an amount to calculate the discount
print("Enter the Amount")
amount = int(input())
final_Amount = 0

# Applying different discounts using 'if-elif-else' based on the amount entered
if amount >= 5000:
    print("Discount eligible: 20%")
    final_Amount = amount - (amount * (20 / 100))
elif amount >= 3500 and amount < 4999:
    print("Discount eligible: 15%")
    final_Amount = amount - (amount * (15 / 100))
elif amount >= 1500 and amount < 3499:
    print("Discount eligible: 10%")
    final_Amount = amount - (amount * (10 / 100))
else:
    # No discount if the amount is below 1500
    print("No discount")
    final_Amount = amount

# Displaying the final amount after discount
print("Final Amount:", final_Amount)

# ------------------------------------------
# Nested if else if
# Check if free tonight and if friends are available for dinner
free_tonight = True
friends_available = False

if free_tonight:
    if friends_available:
        print("Go out for dinner with friends")  # If friends are available, go out for dinner
    else:
        print("Order food and watch a movie")  # If friends aren't available, order food and watch a movie
else:
    print("Cook something at home")  # If not free tonight, cook at home



# <-----------------------------------------------------------------------LOOPS---------------------------------------------------------------------------->
# Loop to print "hello world!" 4 times using a 'for' loop
for i in range(4):
    print("Hello world!")

# ------------------------------------------
# Asking the user to enter a number for generating a multiplication table
print("Enter a number")
num = int(input())

# Using a 'for' loop to print the multiplication table of the entered number
for i in range(1, 11):
    print(num, "x", i, "=", (num * i))

# ------------------------------------------
# Print numbers from 1 to 49 in steps of 5
# Difference: Starts at 1, increments by 5, ends before 50
# Example Output: 1, 6, 11, 16, ..., 46
for i in range(1, 50, 5):
    print(i)

# ------------------------------------------
# Print numbers from 1 to 24
# Difference: Starts at 1, increments by 1 (default), ends at 24
# Example Output: 1, 2, 3, ..., 24
for i in range(1, 25):
    print(i)

# ------------------------------------------
# Print numbers from 0 to 49
# Difference: Starts at 0, increments by 1 (default), ends at 49
# Example Output: 0, 1, 2, ..., 49
for i in range(50):
    print(i)

# ------------------------------------------
# Print numbers from 25 down to 11 in steps of -3
# Difference: Starts at 25, decrements by 3, ends just above 10
# Example Output: 25, 22, 19, ..., 13
for i in range(25, 10, -3):
    print(i)


# ------------------------------------------
# WHILE LOOPS

# Prompt the user to enter a number
print("Enter a number")
num = int(input())  # Convert the input to an integer and store it in the variable 'num'

# Initialize the multiplier 'i' to 1 for the multiplication table
i = 1

# Loop to print the multiplication table of the entered number up to 10
while i <= 10:
    # Print the current multiplication result in the format: num x i = result
    print(num, "x", i, "=", (num * i))
    
    # Increment 'i' by 1 to move to the next multiplier in the next iteration
    i = i + 1

# ------------------------------------------

# Loop asking the user to enter a number until they choose to continue with "yes"
attempt = "no"
while attempt != "yes":
    print("Enter a number:")
    num = int(input())
    print("Square:", num ** 2)  # Print the square of the entered number
    
    print("Continue? yes or no")
    attempt = input().strip().lower()  # Update attempt; convert to lowercase for case-insensitivity

# <-----------------------------------------------------------------------JUMP STATEMENTS---------------------------------------------------------------------------->

# Loop through numbers from 1 to 5
for i in range(1, 6):
    # If i equals 4, exit the loop entirely
    if i == 4:
        break
    # Otherwise, print the current value of i
    print(i)
# Expected output: 1, 2, 3 (the loop stops when i is 4)

# ------------------------------------------

# Loop through numbers from 1 to 5
for i in range(1, 6):
    # If i equals 4, skip this iteration and continue to the next
    if i == 4:
        continue
    # Otherwise, print the current value of i
    print(i)
# Expected output: 1, 2, 3, 5 (the loop skips printing 4)

# ------------------------------------------

# Loop through numbers from 1 to 3
for number in range(1, 4):
    # If number equals 2, do nothing and move to the next statement
    if number == 2:
        pass  
    else:
        # Otherwise, print the current value of number
        print(number)
# Expected output: 1, 3 (number 2 is ignored due to the pass statement)


