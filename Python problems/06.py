# Write a Python program to swap two variables.

# my method
x = 10
y = 20
print(x,y)

t = x
x = y
y = t
print(x,y)
print()  # --> by default \n inside

# or 
def swap(a, b):
    print(a,b)
    temp = a
    a = b
    b = temp
    print(a,b)

swap(10,20)

# or
a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()
