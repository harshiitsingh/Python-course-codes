# Inheritance is a way of creating a new class from an existing class.

class Employee:                            # --> base class or parent class
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):                # --> derived class or child class
    language = "Python"
    # company = "YouTube"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    # def showDetails(self):
    #     print("This is an progrmmer")  # ---> overwriting
    
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)

# Above whole program is a Single inheritance.