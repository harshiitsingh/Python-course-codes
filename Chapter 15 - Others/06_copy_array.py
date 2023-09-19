## Copying an Array in Python

from numpy import *

arr = array([1,2,3,4,5])

arr = arr+5
print(arr)

arr1 = array([6,7,8,9,10])
arr3 = arr+arr1 # This is also called Vectorized Operation
print(arr3)

print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))

# Concatenate Two Arrays
print(concatenate([arr, arr1]))

# Copy

## 1. ALIASING
arr2 = arr1
print(arr1)
print(arr2)

# Do you really have two arrays in the memory?
# No
print(id(arr1))
print(id(arr2))
# Both are pointing to same address. This is called Aliasing. We are creating same alias for same array.
# We can modify the value using arr1 or arr2

# Now if you actually want to create a new array with the different location, then:
arr2 = arr1.view()
print(id(arr1))
print(id(arr2))

# Now, there's one catch here,
## 2. SHALLOW COPY -> when we copy two arrays, then change in one array will reflect in other
arr2 = arr1.view()

arr1[2] = 67
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

## 3. DEEP COPY -> Two same arrays but not linked with each other in anyway.
arr2 = arr1.copy()
arr1[2] = 67
arr2[2] = 69
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))