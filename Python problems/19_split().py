# Write a Python program which accepts
# a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

values = input("Input some comma seprated numbers : ")
list = values.split(",") # Split a string into a list where each word is a list item:
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

'''
The split() method splits a string into a list.

Syntax
string.split(separator, maxsplit)

Parameter	Description
separator :	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit  :	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
'''