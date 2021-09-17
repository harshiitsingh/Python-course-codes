# Enumerate function in Python

list1 = [3,52, False, 6.3, 'harshit']

# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

for index, item in enumerate(list1):
    print(item, index) # prints the items of list1 with index

# Enumerate fxn adds counter to an iterable and returns it