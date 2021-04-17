# A tuple is an immutable(cannot change) data type in python

# Creating a tuple using parenthesis ()
t1 = () # an empty tuple
t2 = (1) # Wrong way to declare a tuple with one elment , its (or python interpreter will take it as) a simple number (and a bracket is used around it)
t3 = (1,) # a tuple with single elment, tuple with only one element needs a comma.
t = (1,2,4,5)
# Printing the elements of a tuple
print(t)
print(t1)
print(t2)
print(t3)
print(t[0])

# We cannot update the values of a tuple
# t[0] = 34   # --> throws an error

# Once defined a tuple elements cant be altered or manipulated