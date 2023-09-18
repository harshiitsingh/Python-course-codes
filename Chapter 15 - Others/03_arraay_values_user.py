## Array values from User in Python | Search in Array

# import array # -> will give error
from array import *

arr = array('i', [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
    
print(arr)

## Search an element
# M-1: Search by manually using loop
val = int(input("Enter the value for search: "))
k = 0
for e in arr: # can also use range
    if(e==val):
        print(k)
        break
    
    k += 1

# M-2: using fxn
print(arr.index(val))