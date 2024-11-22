# What is super()?
# super() is a built-in Python function that allows you to call a method from a parent (or superclass) in a child (or subclass).


# Base class: Parent
class Parent:
    def __init__(self):
        print("Parent Constructor")
        self.a = 10  # Parent class initializes a variable 'a'

    def fun(self):
        print("Parent fun")  # Method in Parent class


# Derived class: Child inherits Parent
class Child(Parent):
    def __init__(self):
        print("Child Constructor")
        self.b = 20  # Child class initializes a variable 'b'
        super().__init__()  # Calls the Parent class constructor
        print("Child b =", self.b)  # Access Child's variable 'b'
        print("Parent a =", self.a)  # Access Parent's variable 'a'

    def fun(self):
        super().fun()  # Calls the Parent class method 'fun'
        print("Child fun")  # Child-specific implementation of 'fun'


# Object creation and method calls
c = Child()  # Instantiate Child, triggers constructors
c.fun()      # Calls 'fun' method of Child, which also calls Parent's 'fun'

# Expected Output for this program:
# Child Constructor
# Parent Constructor
# Child b = 20
# Parent a = 10
# Parent fun
# Child fun


# Second example with multiple inheritance
class Singer:
    def passion(self):
        print("Sing")  # Singer-specific method


class Painter:
    def paints(self):
        print("Paint")  # Painter-specific method


# Derived class: Artist inherits both Painter and Singer
class Artist(Painter, Singer):
    pass  # No additional methods or attributes

# Object creation and method calls
a = Artist()       # Instantiate Artist
a.passion()        # Calls 'passion' from Singer
print(Artist.mro())  # Displays the method resolution order (MRO)

# Expected Output for this program:
# Sing
# [<class '__main__.Artist'>, <class '__main__.Painter'>, <class '__main__.Singer'>, <class 'object'>]

# Since Artist does not define a passion method, it checks its parent classes.
# Based on MRO, it first checks Painter (no match) and then Singer (finds the method).
# Artist.mro() prints the MRO: Artist -> Painter -> Singer -> object.
