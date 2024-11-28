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
