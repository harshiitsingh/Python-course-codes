## Why Numpy?
'''
Using existing array library we can't work on Multi dimension array
'''

# from array import *

# arr = array('i', [2,3,4],[4,5,6])
# arr = array('i', [[2,3,4],[4,5,6]])
# print(arr)

from numpy import *

arr = array([2,3,4,5,6])
print(arr)
arr = array([[2,3,4],[4,5,6]], int) # can also give datatype
print(arr)
