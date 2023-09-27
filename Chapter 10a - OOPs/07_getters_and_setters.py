# since our project is growing so we are going to divide the Parent class and child class in different python files.

# item.py -> will instantiate the objects from CSV
# phone.py -> is the child class of item.py


'''
Getters and Setters are like having a control on our attributes.
'''
from item import Item

item1 = Item("MyItem", 750)

# How to restrict our users to not change the values once initialised/instantiated? i.e., read-only attribute
# ans-> using a property decorator

# Setting an Attribute
item1.name = "OtherItem"

# just for example:
# now we are going to access the property not an attribute
# print(item1.read_only_name) # not item1.read_only_name() -> gives error -> TypeError: 'str' object is not callable
# now try to change the value
# item1.read_only_name = "BBB" # will throw error -> AttributeError: property 'read_only_name' of 'Item' object has no setter

# Getting an Attribute
print(item1.name)