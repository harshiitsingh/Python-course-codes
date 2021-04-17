# An attribute that belongs to the class rather than a particular object.

class Employee:
    company = "Google"  # --> [specific to each class]

harry = Employee()  # --> object instantiation
rajni = Employee()
print(harry.company)
print(rajni.company)

Employee.company = "YouTube"  # --> changing the class attribute
print(harry.company)
print(rajni.company)

# Instace Attributes --> An attribute that belongs to the Instance (object).

# Assuming the class from the previous example : 

harry.name = "Harry"
harry.salary = "30K"  # --> adding instance attributes
harry.salary = 300
rajni.salary = 400
print(harry.salary)
print(rajni.salary)
