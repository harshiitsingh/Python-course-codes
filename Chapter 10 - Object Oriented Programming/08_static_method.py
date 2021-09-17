# In this we do not need to use self parameter.
class Employee:
    company = "Google"

    def getSalary(self, signature): 
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    # def greet(self):
    #     print("Good Morning, Sir")

    @staticmethod
    def greet():  # now here if u put self, it will show an error.
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9 AM in the morning")

harry = Employee()
harry.salary = 100000
# harry.getSalary()
harry.getSalary("Thanks!") 
# harry.getSalary()  # Employee.getSalary(harry)
harry.greet() # Employee.greet()
harry.time()

'''
fxn = method
variable = attribute = properties
these all are interchangeably used in software world.
'''