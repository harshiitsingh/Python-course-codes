## Working with Matrix in Python

## Multidimensional Array

from numpy import *

arr = array([
    [1,2,3,7,8,4],
    [4,5,6,5,9,1]
]) # 2-d array

print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

# convert a 2d array into 1d array
arr1 = arr.flatten()

print(arr1)

# convert a 1d array into 3d
arr2 = arr1.reshape(3,4) # 2d array of size (row,col)
print(arr2)
arr3 = arr1.reshape(2,2,3) # 3d array -> (2 2d array, 2 1d array, Each 1d array have 3 values)
print(arr3)

## Matrices and its operation
arr = array([
    [1,2,3,4],
    [5,6,7,8]
])

m = matrix(arr)
# m = matrix('1 2 3 4 ; 5 6 7 8') # another method to create matrix. If taken from user or string

print(m) # it will give same result as before but provide some more functions to do operations

m = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(diagonal(m))
print(m.min())
print(m.max())

# Adding two matrix

# Multiplication of two matrices
m1= matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2= matrix('1 10 3 ; 1 5 6 ; 7 1 9')

m3 = m1 + m2
print(m3)

m3 = m1 * m2
print(m3)