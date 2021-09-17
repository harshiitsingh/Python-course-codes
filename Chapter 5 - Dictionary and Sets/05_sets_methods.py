# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repetedly does not changes a set
b.add(5)
# Adding list in the set
# b.add([4,5,6])  --> throws error, coz list can be changed or it contents can be later changed
# Adding tuple in the set
b.add((4,5,6)) # can be added coz it cannot be changed
# b.add({4:5}}) # cannot add list or dictionary or any hashable datatype
## Accessing the elements
print(b)

# Length of a set
print(len(b)) # Prints the lenght of this set

# Removal of an Item
b.remove(5) # Removes 5 from set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())
print(b)

b.clear() # empty the set b
print(b)

# union and intersection
# b.union({8,11})
# b.intersection({8,11})