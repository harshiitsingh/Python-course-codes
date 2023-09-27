'''
OOP Principles:
    - Encapsulation
    - Abstraction
    - Inheritance
    - Polymorphism
    
Encapsulation: It is restricting the direct access to some 
of our attributes in a program. Like here we restricted price attribute to change by somebody.
(check item.py -> changes are price to __price and added apply_increment fxn)

Abstraction: hiding unnecessary details from user. This can be done by making methods private.
In other prog lang, it is done by access modifiers.
Here in python it is done by adding double underscores.
eg. def __send_email(): , __body
(Watch again)

Inheritance: Reuse of code across our classes.

Polymorphism: to use of single type entity to represent different types in different scenerios.
'''
# Encapsulation
# from item import Item
# item1 = Item("MyItem", 750) 
# print(item1.price)

# Inheritance and Polymorphism
from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_discount()

print(item1.price)

##  --> https://www.youtube.com/watch?v=Ej_02ICOIgs