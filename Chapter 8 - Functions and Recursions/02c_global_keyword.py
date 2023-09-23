## Global Keyword in Python | Global vs Local Variable

'''
#1 Scope of variable
#2 Local variable
#3 Global variable
#4 Global keyword
#5 Global() function
'''

#1 Scope of variable

a=10 # scope of a is everywhere
def something():
    # a=15 # scope of a is only inside the fxn
    print("In fun", a)

something()
print("Outside fun", a)

'''
-- scope of variable means where we can access the variable
-- there are two types of scope of variable
    1. local scope
    2. global scope

#2 Local variable
-- local variable means variable which is defined inside the function
-- we can access the local variable inside the function only
-- we cannot access the local variable outside the function

Local Scope:
When a variable or function is defined inside a function, it is said to be in the local scope of that function. 
Variables defined in the local scope are only accessible within that function and are destroyed once the function 
completes execution. Local variables have the highest priority in accessing over global variables of the same name.
'''
def func():
    x = 10
    print(x)
func()
# --  the variable x is defined inside the function, and it can only be accessed within the function.

#3 Global variable
# -- global variable means variable which is defined outside the function
# -- we can access the global variable inside the function
# -- we can access the global variable outside the function

x = 10
def func():
    print(x)
func()

# -- the variable x is defined outside the function, and it can be accessed within the function.

#4 Global keyword
# -- if we want to access the global variable inside the function and we want to change the value of 
# global variable inside the function then we have to use global keyword.

x = 10
def func():
    global x
    x = 15
    print(x)
    # x=9 # it will not create a new local varibale x, it will modify x
func()

# -- in this case no new variable is created inside the function, 
# but the global variable x is accessed and modified inside the function.


# Now in above fxn, by using global x, we can't use a local varibale of name x. So how to use that? Use globals fcxn and don't use global keyword
#5 Global() function
# -- if we want to access the global variable inside the function and we want to change the value of  global variable 
# inside the function then we have to use global() function. 

# e.g
x = 10
# print(id(x))
def func():
    x = 15
    print("local x: ",x)
    y = globals()['x']
    print("global x: ",y)
    # print(id(y))
    globals()['x'] = 20 # to change the global variable without affecting local.

func()
# -- using globals()['x'] we can access the global variable x inside the 
# function and we can change the value of global variable x inside the function.