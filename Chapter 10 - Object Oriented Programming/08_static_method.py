
class Employee:
    company = "Google"

    def getSalary(self, signature): 
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    # def greet(self):
    #     print("Good Morning, Sir")

    @staticmethod
    def greet():  # now here if u put self, it will show an error.
        print("Good Morning, Sir")

harry = Employee()
harry.salary = 100000
# harry.getSalary()
harry.getSalary("Thanks!")
harry.greet()

'''
fxn = method
variable = attribute = properties
these all are interchangeably used in software world.
'''