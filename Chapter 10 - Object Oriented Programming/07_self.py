
class Employee:
    company = "Google"
    def getSalary(self): # remove self and see what happens. it will show error.
        # print("Salary is 100k")
        # print(f"Salary is {self.salary}")
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000
harry.getSalary()   # Employee.getSalary(harry) # both will work same