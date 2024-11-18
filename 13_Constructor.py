# Example 1: Mentor class with default attributes and methods
class Mentor:
    def teach(self):
        # Prints a message indicating the mentor is teaching
        print("Mentor teaches")

    def __init__(self):
        # Initializes a mentor with default values
        self.name = "ABC"
        self.tech = "Python"

# Creating an instance of the Mentor class
m = Mentor()

# Displaying mentor's default attributes and calling the teach method
print(m.name)  
print(m.tech)  
m.teach()     

# Sample Output for Example 1:
# ABC
# Python
# Mentor teaches

# -------------------------------------------------------------------------

# Example 2: Mentor class with dynamic attribute initialization
class Mentor:
    def teach(self):
        # Prints a message indicating the mentor is teaching
        print("Mentor teaches")

    def __init__(self, name, tech):
        # Initializes a mentor with dynamic values
        self.name = name
        self.tech = tech

# Creating an instance of the Mentor class with custom attributes
m = Mentor("DEF", "Java")

# Displaying mentor's custom attributes and calling the teach method
print(m.name)  
print(m.tech)  
m.teach()      

# Sample Output for Example 2:
# DEF
# Java
# Mentor teaches

# -------------------------------------------------------------------------

# Example 3: Taking mentor attributes as input from the user
class Mentor:
    def teach(self):
        # Prints a message indicating the mentor is teaching
        print("Mentor teaches")

    def __init__(self, name, tech):
        # Initializes a mentor with user-provided values
        self.name = name
        self.tech = tech

# Taking input for mentor attributes
name = input("Enter the name of a mentor: ")  # Example Input: "Alice"
tech = input("Enter the tech of a mentor: ")  # Example Input: "C++"

# Creating an instance of the Mentor class with user-provided values
m = Mentor(name, tech)

# Displaying mentor's attributes and calling the teach method
print(f"Name: {m.name}")  # Output: Name: Alice
print(f"Tech: {m.tech}")  # Output: Tech: C++
m.teach()                 # Output: Mentor teaches

# Sample Output for Example 3:
# Enter the name of a mentor: Alice
# Enter the tech of a mentor: C++
# Name: Alice
# Tech: C++
# Mentor teaches
