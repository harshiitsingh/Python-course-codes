# The range fxn in Python is used to generate a sequence of numbers.
# We can also specify the start, stop and step-size as:
            #  range(start,stop,step-size)

for i in range(8):  # it will be from 0 to n-1 (here 0 - 7, 8 is not included), by default it will start from 0
    print(i)

for i in range(1, 8):  # it will start from 0 to 7
    print(i)

for i in range(2, 8): # from 2
    print(i)

for i in range(1,8,2): # by default step-size is 1
    print(i)
# usually step-size is not used with range()