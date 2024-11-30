import time
import threading

nums = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'c']

def display_digit(nums):
    for i in nums:
        print(i)
        time.sleep(3)
      
def display_letters(letters):
    for i in letters:
        print(i)
        time.sleep(3)
      
# Create threads, passing the functions and their arguments
t1 = threading.Thread(target=display_digit, args=(nums,))
t2 = threading.Thread(target=display_letters, args=(letters,))

# Start the threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

print("Both threads have finished.")

# Excepted Output
# 1
# a
# 2
# b
# 3
# c
# 4
# d
# 5
# c
# Both threads have finished.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time
import threading

# Function to simulate coding activity
def coding():
    # Prints the current thread's name
    print(f"Hello from {threading.current_thread().name}!")
    for i in range(5):
        print("Coding...")  # Simulates coding work
        time.sleep(1)  # Pause for 1 second between iterations

# Function to simulate error-checking activity
def error_check():
    # Prints the current thread's name
    print(f"Hello from {threading.current_thread().name}!")
    for i in range(5):
        print("Error checking...")  # Simulates error-checking work
        time.sleep(1)  # Pause for 1 second between iterations

# Creating threads for coding and error-checking
t1 = threading.Thread(target=coding, name='Coder')  # Thread for coding
t2 = threading.Thread(target=error_check, name='Tester')  # Thread for error checking

# Start both threads
t1.start()
t2.start()

# Excepted output
# Hello from Coder!
# Coding...
# Hello from Tester!
# Error checking...
# Coding...
# Error checking...

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Daemon thread example
import time
import threading

# Function to simulate a background task running indefinitely
def background_task():
    while True:
        print("Background task is running...")  # Background task message
        time.sleep(1)  # Pause for 1 second between messages

print("Main program starts.")  # Message indicating the main program has started

# Create and start a daemon thread for the background task
thread = threading.Thread(target=background_task)
thread.daemon = True  # This ensures the thread will stop when the main program ends
thread.start()

# Pause the main program for 3 seconds to observe daemon thread output
time.sleep(3)
print("Main program ends.")  # Message indicating the main program has ended

# # Excepted output
# The exact order of Coding... and Error checking... may vary since threads are concurrent.
# The background task message will continue alongside the other threads but stops once the main program ends.

