#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# the Student class encapsulates its properties (roll and name) by initializing them through the constructor. 
# Access to these properties is restricted to controlled methods (get_roll and get_name).
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Class definition with constructor
class Student:
    def __init__(self, roll, name):
        if roll > 0:
            self.roll = roll
        else:
            self.roll = 0
            print("Invalid roll number. Setting roll to 0.")
        
        if len(name) <= 10:
            self.name = name
        else:
            self.name = ""
            print("Invalid name length. Name should have 10 or fewer characters.")

    def get_roll(self):
        return self.roll
    
    def get_name(self):
        return self.name
    

# Using constructor to initialize
st1 = Student(101, "ABCDEFGHIHJKLMNOP")
print("Roll:", st1.get_roll())
print("Name:", st1.get_name())

# Expected Output:
# Invalid name length. Name should have 10 or fewer characters.
# Roll: 101
# Name: 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# the Student class provides setter methods to control how roll and name properties are assigned. 
# Getters are used to access the encapsulated data.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Class definition with setters
class Student:
    def set_roll(self, roll):
        if roll > 0:
            self.roll = roll
        else:
            self.roll = 0
            print("Invalid roll number. Setting roll to 0.")
            
    def set_name(self, name):    
        if len(name) <= 10:
            self.name = name
        else:
            self.name = ""
            print("Invalid name length. Name should have 10 or fewer characters.")

    def get_roll(self):
        return self.roll
    
    def get_name(self):
        return self.name
    

# Using setters to initialize
st2 = Student()
st2.set_roll(101)
st2.set_name("ABC")
print("Roll:", st2.get_roll())
print("Name:", st2.get_name())


# Expected Output:
# Roll: 101
# Name: ABC

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Private Members (__roll):
# Declared with a double underscore (__), making them private.
# Private members can only be accessed using name mangling: (_ClassName__variable)

# Protected Members (_cgpa):
# Declared with a single underscore (_), 
# indicating they are intended for internal use but can still be accessed directly.
                                                                   
# Public Members (name):
# Declared without any underscores and are accessible directly.

class Student:
    def __init__(self):
        self.__roll = 111  # private
        self._cgpa = 7.55  # protected
        self.name = "ABC"  # public

st = Student()

# Accessing private members using Name Mangling (_ClassName__variable)
print(st._Student__roll)  # accessing private member using name mangling
# print(st.__roll)  # ERROR: Direct access to private members is not allowed

# Accessing protected members (using _variable)
print(st._cgpa)  # accessing protected member

# Accessing public members (direct access)
print(st.name)  # accessing public member

# Expected Output:
# 111
# 7.55
# ABC

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
