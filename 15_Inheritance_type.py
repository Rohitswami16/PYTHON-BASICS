# Class representing a Software Engineer with basic methods
class SoftwareEngineer:
    def __init__(self, id, name, salary, company):
        self.id = id
        self.name = name
        self.salary = salary
        self.company = company
    
    # Method to display a general software skill
    def software_skill(self):
        print("I have software skills!")
    
    # Method to introduce the Software Engineer
    def intro(self):
        print(f"ID: {self.id}, Name: {self.name}")
        print(f"Salary: {self.salary}, Company: {self.company}")

# Subclass Tester inherits from SoftwareEngineer and adds its own method
class Tester(SoftwareEngineer):
    def debugging(self):
        print("I have debugging skills!")

# Subclass Developer inherits from SoftwareEngineer and adds its own method
class Developer(SoftwareEngineer):
    def coding(self):
        print("I have coding skills!")

# Creating an instance of Developer class
d = Developer(101, "Suket", 77000, "xyz")
d.intro()            # Inherited method
d.software_skill()    # Inherited method from SoftwareEngineer
d.coding()           # Specific method to Developer

print()

# Creating an instance of Tester class
t = Tester(202, "Shweta", 71000, "xyz")
t.intro()            # Inherited method
t.software_skill()    # Inherited method from SoftwareEngineer
t.debugging()        # Specific method to Tester

# Expected Output:
# ID: 101, Name: Suket
# Salary: 77000, Company: xyz
# I have software skills!
# I have coding skills!

# ID: 202, Name: Shweta
# Salary: 71000, Company: xyz
# I have software skills!
# I have debugging skills!

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Demonstrating constructor and inheritance with different class constructors
class Parent:
    def __init__(self):
        print("Parent constructor")

# Child1 does not override the constructor
class Child1(Parent):
    pass
    
# Child2 overrides the constructor
class Child2(Parent):
    def __init__(self):
        print("Child2 Constructor")

# Creating instances of Child1 and Child2
Child1()  # Output: Parent constructor
Child2()  # Output: Child2 Constructor

# Expected Output:
# Parent constructor
# Child2 Constructor

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Single-Level Inheritance

# Vehicle class with a start method
class Vehicle:
    def start(self):
        print("The Vehicle is starting")

# Car class inherits from Vehicle and adds honk method
class Car(Vehicle):
    def honk(self):
        print("The car is honking, Beep beep!")

# Creating an instance of Car class and calling both methods
c = Car()
c.start()   # Inherited from Vehicle
c.honk()    # Specific to Car

# Expected Output:
# The Vehicle is starting
# The car is honking, Beep beep!
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multiple Inheritance

# Singer class with a sing method
class Singer:
    def sing(self):
        print("Singing a song")

# Painter class with a paint method
class Painter:
    def paint(self):
        print("Painting a picture")

# Artist class inherits from both Singer and Painter (Multiple Inheritance)
class Artist(Singer, Painter):
    pass

# Creating an instance of Artist and calling inherited methods
a = Artist()
a.sing()    # Inherited from Singer
a.paint()   # Inherited from Painter

# Expected Output:
# Singing a song
# Painting a picture
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Multilevel Inheritance

# Vehicle class with start method
class Vehicle:
    def start(self):
        print("The Vehicle is starting")

# Car class inherits from Vehicle and adds honk method
class Car(Vehicle):
    def honk(self):
        print("The car is honking, Beep beep!")

# ElectricCar inherits from Car and adds charge method
class ElectricCar(Car):
    def charge(self):
        print("The electric car is charging")

# Creating an instance of ElectricCar and calling all methods
ec = ElectricCar()
ec.start()   # Inherited from Vehicle
ec.honk()    # Inherited from Car
ec.charge()  # Specific to ElectricCar

# Expected Output:
# The Vehicle is starting
# The car is honking, Beep beep!
# The electric car is charging

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hierarchical Inheritance

# Appliance class as a base class with a plug_in method
class Appliance:
    def plug_in(self):
        print("The appliance is plugged in.")

# Subclass WashingMachine inherits Appliance and adds wash_clothes method
class WashingMachine(Appliance):
    def wash_clothes(self):
        print("The washing machine is washing clothes.")

# Subclass Refrigerator inherits Appliance and adds cool_food method
class Refrigerator(Appliance):
    def cool_food(self):
        print("The refrigerator is cooling food.")

# Creating instances of WashingMachine and Refrigerator
washer = WashingMachine()
fridge = Refrigerator()

washer.plug_in()       # Inherited method
washer.wash_clothes()  # Specific to WashingMachine

fridge.plug_in()       # Inherited method
fridge.cool_food()     # Specific to Refrigerator

# Expected Output:
# The appliance is plugged in.
# The washing machine is washing clothes.
# The appliance is plugged in.
# The refrigerator is cooling food.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hybrid Inheritance

# Vehicle class with a start method
class Vehicle:
    def start(self):
        print("The vehicle is starting.")

# Car class inherits from Vehicle and adds honk method
class Car(Vehicle):
    def honk(self):
        print("The car is honking. Beep beep!")

# Electric class adds charge method
class Electric:
    def charge(self):
        print("The vehicle is charging.")

# ElectricCar inherits from both Car and Electric (Hybrid Inheritance)
class ElectricCar(Car, Electric):
    def drive(self):
        print("The electric car is driving silently.")

# Creating an instance of ElectricCar and calling all methods
electric_car = ElectricCar()
electric_car.start()    # Inherited from Vehicle
electric_car.honk()     # Inherited from Car
electric_car.charge()   # Inherited from Electric
electric_car.drive()    # Specific to ElectricCar

# Expected Output:
# The vehicle is starting.
# The car is honking. Beep beep!
# The vehicle is charging.
# The electric car is driving silently.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
