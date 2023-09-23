## Types of Arguments in Python
def add(a,b): # Formal Arguments
    c = a+b
    return c

add(5,6) # Actual Arguments

'''
There are two types of Arguments:
- Formal -> at the time of define
- Actual -> at the time of fxn call. There are more types of actual arguments
    - Position
    - Keyword
    - Default
    - Variable Length
'''

def person(name, age): # age=18 # this is default
    print(name)
    print(age - 5)
    
person('harshit', 22) # this is position, where position of arguments matter
# person(22, 'harshit') # will give error
person(age = 22,name = 'harshit') # this is keyword, when you forgot the actual position of argument but know their names only.


## Variable Length Argument -> No. of argument is not fixed in the fxn
def sum(a,*b): # *b means it can accept multiple values
    # c=a+b
    print(a)
    print(b)
    # print(c)
    
    c = a
    # c = 0
    for i in b:
        c=c+i
    print(c)

sum(5,6,34,78)

## Keyworded Variable Length Arguments in Python | **kwargs
'''
Special Symbols Used for passing arguments in Python:
    - *args (Non-Keyword Arguments)
    - **kwargs (Keyword Arguments)

-->  https://www.geeksforgeeks.org/args-kwargs-python/
-->  https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/

Variable length argument :
-- A variable-length argument is a feature that allows a function to accept an arbitrary number of arguments. 
The syntax for defining a variable-length argument in Python is to use an asterisk (*) before the parameter name.
e.g
def person(name,*data):
    print(name)
    print(data)
person('navin',28,9765432)

keyword variable length argument:
-- keyword variable length argument is a feature that allows a function to accept an arbitrary number of keyword arguments.
-- use a double asterisk (**) to define a variable-length argument that accepts keyword arguments. For example:
--  the **kwargs parameter allows the function to accept an arbitrary number of keyword arguments. 
    The function can then loop over the dictionary of keyword arguments and do something with them.

e.g

'''
def person(name,**data):  #**kwargs
    print(name)
    for i, j in data.items():
        print(i,j)  #i is key and j is value
        
person('navin',aget=28,city='Mumbai',mob=9865432)