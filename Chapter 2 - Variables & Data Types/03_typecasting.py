a = "3434"

print(type(a))
# print(a+5) error coz adding stirng to integer

a = int(a)
print(type(a))
print(a+5)
'''
a = "34ggger777"
a = int(a)
invalid literal     cant converted to integer
'''

b = 5.6
c = int(b)
print(type(b))
print(type(c))
print(c)

k = float(c)
print(k)

d = complex(c, k)
print(d)


print(int(True))
print(int(False))

## How to convert a range into a list?
print(list(range(10))) ## we can do for loop also.

print(list(range(2, 10, 2)))