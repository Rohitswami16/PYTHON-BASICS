from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):  # Added ABC as the base class for using @abstractmethod
    @abstractmethod
    def eat(self):  # Abstract method to be implemented by subclasses
        pass

    @abstractmethod 
    def sleep(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Concrete class: Dog
class Dog(Animal):
    def eat(self):
        print("Dog is eating")

    def sleep(self):
        print("Dog is sleeping at home")

    def move(self):
        print("Dog is moving at 10 km/hr")

# Concrete class: Tiger
class Tiger(Animal):
    def eat(self):
        print("Tiger is eating non-vegetarian food")

    def sleep(self):
        print("Tiger is sleeping in a cave")

    def move(self):
        print("Tiger is moving at 90 km/hr")

# Concrete class: Monkey
class Monkey(Animal):
    def eat(self):
        print("Monkey is eating bananas")

    def sleep(self):
        print("Monkey is sleeping on a tree")

    def move(self):
        print("Monkey is moving at 30 km/hr")

# Function to access animal methods
def accessAnimal(an):
    an.eat()
    an.sleep()
    an.move()

# Creating objects and accessing their methods
d = Dog()
accessAnimal(d)

t = Tiger()
accessAnimal(t)

m = Monkey()
accessAnimal(m)

# This line would raise an error because Animal is abstract and cannot be instantiated
# a = Animal()
# accessAnimal(a)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Expected Output

# Dog is eating
# Dog is sleeping at home
# Dog is moving at 10 km/hr
# Tiger is eating non-vegetarian food
# Tiger is sleeping in a cave
# Tiger is moving at 90 km/hr
# Monkey is eating bananas
# Monkey is sleeping on a tree
# Monkey is moving at 30 km/hr
