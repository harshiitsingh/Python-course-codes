a = 3
b = 4

# 1. Arithmetic operator
print(3+4)
print("The value of 3+4 is",3+4)
print("The value of 3+4 is",a+b)
print(8+2)
print("The value of 3-4 is",3-4)
print("The value of 3*4 is",3*4)
print("The value of 3/4 is",3/4) # try 8/4 # --> Floating Point Representation
print("The value of 3//4 is",3//4) # try 8/4 # gives only integer/quotient. Integer Division
print("The value of 3%4 is",3%4) # try 8/4

# 2. Assignment operators
a = 34
a += 2 # or a = a+2
print(a)
a /= 2
print(a)

a,b = 5,6 # assignment in one line of 2 variables
print(a)
print(b)

# 3. Relational/Comparison operator --> returns boolean
print(a==b) # not same as assignment operator
print(a!=b)
b = (14<7)
b = (14>=7)
print(b)

# 4. Logical operators --> used to compare two conditions
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is",(bool1 and bool2))
print("The value of bool1 or bool2 is",(bool1 or bool2))
print("The value of not bool2 is",(not bool2))

# 5. Unary Operators
n = 7
print(-n)
n = -n # negation
print(n)

#to find remainder
print(34%2)

# You can control the order of operations in long calculations with parentheses.
print(((1 + 3) * (9 - 2) / 2) ** 2)

# In general, Python follows the PEMDAS rule when deciding the order of operations.
'''
P -> Parentheses first
E -> Exponents (ie Powers and Square Roots, etc.)
MD -> Multiplication and Division (left-to-right)
AS -> Addition and Subtraction (left-to-right)
'''