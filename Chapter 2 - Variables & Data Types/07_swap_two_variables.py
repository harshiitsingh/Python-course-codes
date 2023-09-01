## Swap 2 Variables in Python

a = 5 # 101 -> 3 bits
b = 6 # 110 -> 3 bits
# Before Swap
print(a)
print(b)

## Method-1
# temp = a
# a = b
# b = temp

## Method-2: Without using 3rd variable-> Memory Efficient
# Using a formula
# a = a+b # 11 -> 4 bits. Means taking some extra bits. Therefore, XOR method
# b = a-b # 5
# a = a-b # 6

## Method-3: Using XOR
# a = a^b
# b = a^b
# a = a^b

## Method-4: Unique to Python Only
a,b = b,a 
'''
But how does it work?

System will solve RHS first. So b,a will go into the stack
And then it will do ROT_TWO() -> Swaps the two top-most stack items.
And finally the value will be assigned to LHS.
'''

# After Swap
print(a)
print(b)