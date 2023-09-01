## Number System Conversion in Python

'''
In programming, there are two formats, one is binary and one is decimal.
Besides, there are two more, one is octal and one is Hexadecimal.

Now when to use these?
In computer -> Binary System
Physical address/MAC Addr -> Hexadecimal Format
IPv6 -> Hexadecimal Format

How to convert from one format to other?
'''

# Decimal (Base is 10) -> 0-9
# Binary (Base is 2) -> 0-1 (BIT -> BInary digiT)

# Decimal to Binary
print(bin(25))

# Binary to Decimal
print(0b0101)

# Octal(base is 8) -> 0-7
# Hexadecimal (base is 16) -> 0-9 a-f

# Decimal to Octal
print(oct(25))

# Decimal to Hexadecimal
print(hex(25))

# Hexadecimal to Decimal
print(0xf)