greeting = "Good Morning, "
name = "Harry"
# concatenating two strings
print(greeting + name)
c = greeting + name
print(c)

# Indexing of a string
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # IndexError: string index out of range

# name[3] = "d" --> does not work, we can access a character or element of a string but cannot change
# name[3:] = "gh"
'''
Strings in Python are IMMUTABLE.
https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python/

But can do:
print("Hi" + name)
print("Hi" + name[3:])
'''


# String slicing
print(name[0:3])
print(name[0:4])
print(name[1:4]) # --> first one is included 2nd one excluded
print(name[:4])  # is same as name[0:4]
print(name[1:])  # is same as name[1:5]

# Negative indices
print(name[-1])
print(name[-4:-1])

c = name[-4:-1]  # is same as name[1:4]
print(c)

# Slicing with skip value
d = name[1:4:1]
e = name[1:4:2]
f = name[::-1]
print(d)
print(e)
print(f)

name = "HarryIsGood"
d = name[0::2]
print(d)
d = name[0::3]
print(d)