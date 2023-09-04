
## How to take input from command line?
## Use argv

import sys
# argv[0] is the file name
x = int(sys.argv[1]) # also it will give the string, so convert into int
y = int(sys.argv[2])
z = x+y
print(z)