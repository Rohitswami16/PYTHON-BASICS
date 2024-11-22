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
