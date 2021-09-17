# Q.2 Write a program that takes a string as input and
# prints the number of occurrences of each character in the string.

str = input("Input a string: ")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
    
print(dict)