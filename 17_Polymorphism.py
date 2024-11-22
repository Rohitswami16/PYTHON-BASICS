# Base class: Robot
class Robot:
    """
    The base class `Robot` defines common methods (`talk`, `walk`, `charge`) 
    that will be inherited by all derived classes.
    """
    def talk(self):
        print("Robo can talk")

    def walk(self):
        print("Robo can walk")

    def charge(self):
        print("Robo can charge")


# Derived class: FighterRobo
class FighterRobo(Robot):
    """
    The `FighterRobo` class inherits from `Robot` and adds its own unique method `fight`,
    demonstrating that it has additional capabilities beyond the base class.
    """
    def fight(self):
        print("Robo can fight")


# Derived class: TeacherRobo
class TeacherRobo(Robot):
    """
    The `TeacherRobo` class inherits from `Robot` and adds its own unique method `teach`,
    showing polymorphic behavior when used in the context of `access_robo`.
    """
    def teach(self):
        print("Robo can teach")


# Derived class: DriverRobo
class DriverRobo(Robot):
    """
    The `DriverRobo` class inherits from `Robot` and adds its own unique method `drive`.
    This showcases the concept of polymorphism when accessed dynamically.
    """
    def drive(self):
        print("Robo can drive")


# Function to access Robot features
def access_robo(r):
    """
    This function demonstrates polymorphism:
    - The same function `access_robo` can handle different types of objects (`FighterRobo`, `TeacherRobo`, `DriverRobo`).
    - It calls methods (`talk`, `walk`, `charge`) that are common to all types of robots.
    - It dynamically checks the type of robot (`isinstance`) and calls specific methods (`fight`, `teach`, `drive`) based on the object type.
    """
    r.talk()  # Calls the common method `talk`
    r.walk()  # Calls the common method `walk`
    r.charge()  # Calls the common method `charge`

    # Dynamically check the object type and call its unique method
    if isinstance(r, FighterRobo):
        r.fight()  # Calls the `fight` method if it's a FighterRobo
    elif isinstance(r, TeacherRobo):
        r.teach()  # Calls the `teach` method if it's a TeacherRobo
    elif isinstance(r, DriverRobo):
        r.drive()  # Calls the `drive` method if it's a DriverRobo


# Instantiate and test FighterRobo
f = FighterRobo()  # Create an object of FighterRobo
access_robo(f)  # Calls common and specific methods for FighterRobo

# Instantiate and test TeacherRobo
t = TeacherRobo()  # Create an object of TeacherRobo
access_robo(t)  # Calls common and specific methods for TeacherRobo

# Instantiate and test DriverRobo
d = DriverRobo()  # Create an object of DriverRobo
access_robo(d)  # Calls common and specific methods for DriverRobo

# Expected Output:
# Robo can talk
# Robo can walk
# Robo can charge
# Robo can fight  # Unique to FighterRobo
# Robo can talk
# Robo can walk
# Robo can charge
# Robo can teach  # Unique to TeacherRobo
# Robo can talk
# Robo can walk
# Robo can charge
# Robo can drive  # Unique to DriverRobo

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Demonstrates method overloading using variable arguments (*args)
class Addition:
    def add(self, *args):
        print("Sum =", sum(args))  # Computes the sum of all arguments


a = Addition()
a.add(10, 20)               # Calls add with two arguments
a.add(10, 20, 30)           # Calls add with three arguments
a.add(10, 20, 30, 40)       # Calls add with four arguments

# Expected Output:
# Sum = 30
# Sum = 60
# Sum = 100

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Circle class demonstrates operator overloading
class Circle:
    def __init__(self, rad):
        self.rad = rad  # Initializes the radius

    def __add__(self, other):
        return self.rad + other.rad  # Overloads '+' for adding radii of two Circle objects

    def __str__(self):
        return f"Circle object with radius {self.rad}"  # String representation of a Circle object


# Create Circle instances
c1 = Circle(10.5)
print("Area of c1: ", (3.14 * c1.rad * c1.rad))  # Calculate and print area of c1

c2 = Circle(20.5)
print("Area of c2: ", (3.14 * c2.rad * c2.rad))  # Calculate and print area of c2

# Demonstrate overloaded operators
print("Sum of radii = ", (c1.rad + c2.rad))  # Adding radii as floats
print("Sum of radii = ", (c1 + c2))         # Adding using overloaded '+' operator

# Print Circle objects (uses the overloaded __str__ method)
print(c1)
print(c2)

# Expected Output:
# Area of c1:  346.185
# Area of c2:  1320.865
# Sum of radii =  31.0
# Sum of radii =  31.0
# Circle object with radius 10.5
# Circle object with radius 20.5

