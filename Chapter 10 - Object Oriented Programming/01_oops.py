'''
Solving a problem by creating objects is one of the most popular approaches
in programming. This is called OOP.

This concept focuses on using reusable code.
OOP implements DRY principle. (DRY --> DO NOT REPEAT YOURSELF).
(Functions also implements DRY peinciple)
'''

a = 12
b = 34
print("The sum of a and b is ", a+b)
# above one is normal method which is called PROCEDURAL ORIENTED PROGRAMMING.

# Now this same code or to sum two numbers through OOP :
class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

'''

CLASS AND OBJECT :
Class - a blueprint (a simple railway form). 
        It does not take memory in space (means do not form instance) but code will take memory.

        syntax: 
        class Employee:  [class name is written in Pascal scale]
            # methods & variables
        
        {
            Now PascalCase e.g. --> EmployeeName etc
            And camelCase e.g. --> isNumeric, isFloat, isFloatOrInt etc
        }
Object - a whole application form after filling.
         An object is an instantiation of a class. When class is defined, a template(info)
         is defined. Memory is allocated only after object instantiation.
         
         Objects of a given class can invoke the methods available to it without the implementation
         details of the user.  ----> ABSTRACTION and ENCAPSULATION

'''