'''
NOTE :
Instance attributes take prefernce over class attributes during assignment and retreival.

harry.attribute1  ---> 1) Is attribute1 present in object?
                       2) Is attribute1 present in class?
'''

class Employee:
    company = "Google"  
    salary = 100
 
rajni = Employee()
harry = Employee()

# creating instance attribute salary for both the objects.
# harry.salary = 300
# rajni.salary = 400
harry.salary = 45
print(harry.salary)
print(rajni.salary)
# print(rajni.address)  # --> throws  an 'attribute error', as address is not present in instance/class.
