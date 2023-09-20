## Function Arguments in Python
'''
Big Project -> Break into smaller tasks -> Each task can be represented as functions

Those things are reusable.

- Concept of Modularity
'''

def update(x): # l
    print(id(x)) # before updating x
    x = 8
    print(id(x)) # after updating x
    # as you change the value of x in line 12, its assigned a new variable with new address/memory
    # because string and integer are immutable.
    
    # let's pass something mutable
    # l[2] = 17
    print(x)

update(10)

a = 12
print(id(a))
update(a)
print(a) # will the value of a be updated? No

'''
- Pass by value
- Pass by reference

In above line 21, a is passed by value, so it's actual value present in the 
address/memory will not be affected.

In python, everything is about object.
There is no concept of pass by value and reference in python. None of them is used.
'''

# What if we pass something mutabel?
l = [12,1,3,14]
print(id(l[2]))
update(l[2])
print(l[2]) # will the value of l[2] be updated? No