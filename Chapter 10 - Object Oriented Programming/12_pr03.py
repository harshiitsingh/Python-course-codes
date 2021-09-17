'''
Create a class with a class attribute a ; 
create an object from it and set a directly using object a = 0.
Does this change the class attribute?
'''

class Sample:
    a = "Harry"

obj = Sample()
obj.a = "Vicky" # it will create a new instance attribute not change it
# Sample.a = "Vicky"  # it will change the class attribute

print(Sample.a)
print(obj.a)