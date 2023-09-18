## Array in python don't have fixed size. Ut can expanded anytime.
## Array is of same datatype elemets.

# import array as arr

# arr.array()

## or
from array import *

## Search type code in python for arrays.

vals = array('i', [5,9,-8,4,2]) # 'i' is signed int Type Code and 'I' is unsigned int

print(vals)
print(vals.typecode)
print(vals.buffer_info()) # gives (address of array, size of array)
# print(vals.reverse()) # Output is None because reverse don't have any return type/value
# vals.reverse()
# print(vals)

## Print each values
# print(vals[2])
for i in range(5): # if we don't know the length or want to make more dynamic use-> range(len(vals)):
    print(vals[i])

## or -> more dynamic
for e in vals:
    print(e)
    
## Creating new array with the existing array
newArr = array(vals.typecode, (a for a in vals)) # if you don't know the typecode and values of previous array.
newArr = array(vals.typecode, (a*a for a in vals))
print(newArr)

i = 0
while i<len(newArr):
    print(newArr[i])
    i+=1

## Working with Unicode or Chars
vals = array('u', ['a', 'i', 'e'])
