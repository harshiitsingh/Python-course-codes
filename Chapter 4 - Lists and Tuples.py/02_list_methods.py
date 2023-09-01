l1 = [1,8,7,2,22,15]
print(l1)
# 1
l1_sorted = l1.sort() # Here l1 will changed, hence print none
print(l1_sorted)

l1.sort()
print(l1)
print(l1.sort())
print(l1.sort())

# 2
l1.reverse()
print(l1)

# 3
l1.append(45) # appends or adds (45) at the end of the list
# GOOGLE MEANING OF APPEND # will most used (ALSO in web scrapping and ML)
l1.append(90)
print(l1)

# 4
l1.insert(0,544) # inserts 544 at index 0
l1.insert(2,44)
print(l1)

# 5
l1.pop(2) # removes element at index 2
print(l1)

l1.pop() # if use pop without index value --> it will same as stack and pop the last item
print("Pop without index", l1)

# 6
l1.remove(22) # removes 22 from the list
print(l1)

# 7
del l1[3:6] # want to delete multiple values from the list.
print("Multiple Values deleted:", l1)

# 8
l1.extend([54, 69, 100]) # to add multiple elements.
print(l1)

# We can never write all the list methods, there are lots of list methods and with time more methods would come
# so simply google "list methods python docs" from official python documentation
# Python docs are best


### Now perform some in-built fxns on the list
print(min(l1))
print(max(l1))
print(sum(l1))