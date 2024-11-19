# Static Method (goto_team_outing): Executes a general task unrelated to instance attributes.
# Class Method (change_company_name): Updates the shared company name across all employees.
# Instance Methods (do_job, intro): Operate on instance-specific attributes like eid, ename, and esalary.
# Dynamic Company Name Change: Prompt user input to update the company name for all employees.

                                                                         
class Employee:
    ecompany = "XYZ Company"  # Class attribute

    @staticmethod
    def goto_team_outing():
        print("Go to team outing...")  # Static method

    @classmethod
    def change_company_name(cls, new_name):
        cls.ecompany = new_name  # Class method to change the company name

    def __init__(self, eid, ename, esalary): 
        self.eid = eid         # Instance attributes
        self.ename = ename
        self.esalary = esalary

    def do_job(self, role):
        self.role = role       # Assign job role
        print(f"My job role is: {self.role}")

    def intro(self):
        # Print employee details and company
        print(f"ID: {self.eid}, Name: {self.ename}, Salary: {self.esalary}, Company: {Employee.ecompany}")


# Change company name using class method
name = input("Enter new company name: ")
Employee.change_company_name(name)

# Create and display details for employees
e1 = Employee(101, "Alice", 50000)
e1.do_job("Software Engineer")
e1.intro()
Employee.goto_team_outing()
print()

e2 = Employee(102, "Bob", 60000)
e2.do_job("Test Engineer")
e2.intro()
Employee.goto_team_outing()
print()

e3 = Employee(103, "Smith", 45000)
e3.do_job("Data Scientist")
e3.intro()
Employee.goto_team_outing()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# INPUT
# Enter new company name: ABC Corp

# OUTPUT
# My job role is: Software Engineer  
# ID: 101, Name: Alice, Salary: 50000, Company: ABC Corp  
# Go to team outing...  

# My job role is: Test Engineer  
# ID: 102, Name: Bob, Salary: 60000, Company: ABC Corp  
# Go to team outing...  

# My job role is: Data Scientist  
# ID: 103, Name: Smith, Salary: 45000, Company: ABC Corp  
# Go to team outing...
