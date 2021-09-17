
def square(num):
    return num*num

l = [1, 2,4]
# now we want to print the sqaure of each number in the list

# method 1
l2 = []
for item in l:
    l2.append(square(item))

print(l2)

# Method 2
'''
Map applies a function to all the items in an input list
syntax:
        map(function, input_list) # function can be lambda function
'''
# print(map(square, l))
print(list(map(square, l))) # typecast into list