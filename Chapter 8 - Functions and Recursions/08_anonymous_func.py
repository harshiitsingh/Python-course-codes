## Anonymous Functions | Lambda

# Functions without name is called anonymous or lambda fxns.

# def square(a):
#     return a * a
#
# result = square(5)
#
# print(result)

'''
A lambda function can take any number of arguments, but can only have one expression.

A fxn that can be used once and you don't want to define the name of the fxn.

--> https://realpython.com/python-lambda/

-- We can pass fxn to a fxn, the way you pass objects and values to a fxn.
    Similarly, we can pass fxns, because fxns are objects in Python.
'''

f = lambda a,b : a+b # fxns are objects in the python, so instantiated/assigned.

result = f(5,6)

print(result)