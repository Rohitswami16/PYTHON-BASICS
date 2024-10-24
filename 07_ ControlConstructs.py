# ------------------------------------------

# Control Constructs in Python
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
# LOOPS
# Loop to print "hello world!" 4 times using a 'for' loop
for i in range(4):
    print("Hello world!")

# ------------------------------------------
# LOOP 
# Asking the user to enter a number for generating a multiplication table
print("Enter a number")
num = int(input())

# Using a 'for' loop to print the multiplication table of the entered number
for i in range(1, 11):
    print(num, "x", i, "=", (num * i))
