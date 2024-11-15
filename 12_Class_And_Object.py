# Define the Mentor class
class Mentor:
    # Method to define initial states (attributes) of a Mentor
    def define_states(self):
        self.name = "ABC"  # Name of the mentor
        self.tech = "Python"  # Technology expertise
        self.salary = 25000  # Salary of the mentor

    # Method to simulate teaching by the mentor
    def teaching(self):
        print(f"{self.name} is teaching {self.tech}")

    # Method to indicate the mentor grooms students
    def grooming(self):
        print("Mentor grooms students")

    # Method to display the mentor's information
    def mentorInfo(self):
        print(f"Name: {self.name}, Tech: {self.tech}, Salary: {self.salary}")


# Create an object of the Mentor class
m = Mentor()
m.define_states()  # Set the initial states
m.teaching()  # Call the teaching method
m.grooming()  # Call the grooming method
m.mentorInfo()  # Display mentor information

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define the Student class
class Student:
    # Method to define initial attributes for a student
    def define_status(self):
        self.Id = 101  # Student ID
        self.name = "ABC"  # Student's name
        self.branch = "CS"  # Branch of study
        self.YOP = 2024  # Year of passing

    # Method to display the student's information
    def studentInfo(self):
        print(f"ID: {self.Id}, Name: {self.name}, Branch: {self.branch}, YOP: {self.YOP}")

    # Method to simulate the student studying
    def study(self):
        print("Student is studying")

    # Method to simulate the student giving interviews
    def giveInterviews(self):
        print("Student is giving interviews")


# Create an object of the Student class
student = Student()
student.define_status()  # Set the initial attributes
student.study()  # Call the study method
student.giveInterviews()  # Call the giveInterviews method
student.studentInfo()  # Display student information

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define the Students class to showcase basic attributes and methods
class Students:
    # Method to simulate a student studying programming
    def study(self):
        print("Student studies programming")


# Create an object of the Students class
s = Students()
s.roll = 101  # Assign roll number to the student
s.name = "ABC"  # Assign name to the student

# Display student details
print("Roll:", s.roll)
print("Name:", s.name)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define the Car class
class Car:
    # Method to set car attributes and simulate driving
    def drive(self):
        self.brand = "BMW"  # Brand of the car
        self.price = 205100  # Price of the car
        print("Driving the car")


# Create an object of the Car class
c = Car()
c.drive()  # Call the drive method
# Display car details
print(f"Brand: {c.brand}, Price: {c.price}")
