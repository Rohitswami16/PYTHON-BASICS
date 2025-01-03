# Function to calculate the sum of digits of a given number
def findSum(n):
    sum = 0  # Initialize sum to store the sum of digits
    
    # Loop to extract and sum each digit of the number
    while n != 0:
        dig = n % 10       # Get the last digit of n
        sum = sum + dig    # Add the extracted digit to sum
        n = n // 10        # Remove the last digit from n by integer division
    
    return sum  # Return the sum of the digits
    
# Test the function with an example
sum = findSum(65)
print(f"The sum of the digits is {sum}")
   
OUTPUT: The sum of the digits is is 11

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Get the number of terms for the Fibonacci sequence from user input
n = int(input("Enter the number of terms: "))

# Initialize the first two terms of the Fibonacci sequence
a = 0  # First term
b = 1  # Second term

# Loop to calculate and print the Fibonacci sequence up to n terms
for i in range(1, n + 1):
    print(a, end=" ")  # Print the current term

    # Update the values of a and b to get the next term
    temp = a + b  # Calculate the next term in the sequence
    a = b         # Move 'b' to 'a' for the next iteration
    b = temp      # Update 'b' to the new term (temp)

INPUT : 6
OUTPUT: 0 1 1 2 3 5

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

