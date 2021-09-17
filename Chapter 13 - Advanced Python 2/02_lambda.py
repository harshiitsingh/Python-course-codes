# LAMBDA FUNCTION :
# Functions creatd using an expression using lambda keyword.
# and this function can be used as a normal functions

# def func(a):
#     return a+5

func = lambda a: a+5
square = lambda x: x * x
sum = lambda a,b,c: a+b+c

x = 3
print(func(x))
print(square(x))
print(sum(x, 1, 2))