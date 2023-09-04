# Import Math Functions in Python

import math
x = math.sqrt(25)
print(x)

print(math.sqrt(15))

# floor function
print(math.floor(2.9))
print(math.floor(2.2))
# ceil function
print(math.ceil(2.9))
print(math.ceil(2.2))

# Power
print(3 ** 2)
print(math.pow(3,2)) # when you use/work on big projects/softwares you always use functions.

print(math.pi)
print(math.e)

## Concept of Alias
import math as m
print(math.sqrt(25))
print(m.sqrt(25))

## When you import math, you import everything. If you want to import only specific functions or classes.

from math import sqrt, pow
print(pow(4,5))
# print(help('math')) # Read documentation for more details.