## Ways of Creating Arrays in Numpy

from numpy import *

# M-1
arr = array([1,2,3,4,5]) # you can give the type parameter but no need for that, it'll automatically guess the type.

print(arr)
print(arr.dtype)

arr1 = array([1,2,3,4,5.0])
# arr1 = array([1,2,3,4,5], float)

print(arr1)
print(arr1.dtype) # we are not doing explicitally, so implicit conversion comes into picture.

# M-2
arr = linspace(0, 16, 10) # it will break into 10 parts from 0 to 16, both inclusive.
# by default it will divide into 50 parts, if not specified.
print(arr)

# M-3
arr = arange(0, 16, 2) # 2 is no. of steps
print(arr)

# M-4
arr = logspace(1, 40, 5)
print(arr)
print('%.2f' %arr[0])

# M-5
arr = zeros(5)
print(arr)

arr = zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
print(arr)

# M-6
arr = ones(5) # by default will give float values, 1.0
arr = ones(5, int)
print(arr)