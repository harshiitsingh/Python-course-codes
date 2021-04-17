class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

# to change or add class attribute:

    # def changeSalary(self,sal):
    #     # self.salary = sal
    #     self.__class__.salary = sal

# or

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal


e = Employee()
print(e.salary)
print(Employee.salary)

e.changeSalary(455)
print(e.salary)
print(Employee.salary)