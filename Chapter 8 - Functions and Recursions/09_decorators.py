## Decorators
'''
- Properties of functions
- What are decorators in Python?
- How to add extra features to a function?
- Properties of Decorators
- How to define decorators in Python?

#1
- Functions are built to perform certain tasks.

Properties of functions:-
- We can also write a code for the function inside another function.
- We can assign a function to another function in python as a function is also an object.
- A function is an instance of the Object type.
- We can store the function in a variable.
- We can also pass the function as a parameter to another function.
- A function from a function can also be returned.

#2
- Decorators are used to add extra features to the existing functions.
- Decorators can change the behaviour of an existing function at the compile itself.

#3
Properties of Decorators:-
-The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.
- Decorator contains an outer function that also takes a function as an argument.
- Inside the outer function, there is another function that takes a number of parameters as per the logic as an argument.
- Inner function contains the code for the logic that must be contained in the previously defined normal function.
- Inner function returns the values as per the required code that can be equal to the number of arguments passes in an inner function.
- Outer function return an inner function.
- In the main code, we have to call the outer function of a decorator and pass the normal function as an argument.
'''


# def div(a,b):
#     print(a/b)
#
# div(2,4)


# def div(a,b):
#     if a<b:
#         a,b = b,a
#     print(a/b)
#
# div(2,4)

def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):

        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

div = smart_div(div)

div(2,4)