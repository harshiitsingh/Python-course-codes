# Create a list using []
a = [1,2,4,7,3,56,9]
a1 = [1, 2, 4, 7, 3, 56, 9]

# Print the list using prinr() function
print(a)
print(a1)

# Access using index using a[0], a[1].......
print(a[0])
print(a[1])
print(a[4])
# print(a[7]) --> Error

# Change the value of list using --> LISTS are MUTABLE
a[0] = 98
print(a)

# We can create a list with items of different types
c = [45, "Harry", False, 6.9]
print(c)

# List slicing
freinds = ["Harry", "Harshit", "Ayushi", "Harsh", "Nishant", 45]
print(freinds[0:4])
print(freinds[-4:])