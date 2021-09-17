# __init__() constructor
# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also k/a constructor
# It takes self argument and can also take further arguments.
# It is called constructor bcoz it iniitialises the object

class Employee:
    company = "Google"

    # def __init__(self):
    #     # super().__init__()
    #     print("Employee is created.")

    # def __init__(self, name, salary, subunit): # we have to pass these parameters here otherwise if run without pass it will show error...try it
    #     print("Employee is created.")  # self will automatically passed.

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        self.a = 0
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The subunit of the Employee is {self.subunit}")

    def getSalary(self, signature): 
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

# harry = Employee()
harry = Employee("Harry", 100, "YouTube") # now the program will run successfully as parameters here are passed..although not used in the class or function
# harry = Employee() # This throws an error (missing 3 required positional arguments:)
harry.getDetails()
