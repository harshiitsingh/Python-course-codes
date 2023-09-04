a = input("Enter your name: ")
print(a) 
print(type(a)) # this function allow users to take input as string
a = int(a)
print(a)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(x+y)

## How to take a character only as a input?
# ch = input('Enter a char') # But user might enter more than 1 character
# print(ch[0])
ch = input('Enter a char')[0] # to select only first character of the user input string

print(ch)

## eval function
result = eval(input('enter an expression: ')) # e.g. 2+8-1
print(result)
