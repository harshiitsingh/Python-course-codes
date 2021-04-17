# Q.1 Write a program to find greatest of four numbers entered by the user.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

# if a>b and a>c and a>d:
#     print(a,"is greatest number")
# elif b>a and b>c and b>d:
#     print(b,"is greatest number")
# elif c>a and c>b and c>d:
#     print(c,"is greatest number")
# else:
#     print(d,"is greatest number")

# OR USING NESTING

# if a>d:
#     if a>c:
#         if a>b:
#             print(a,"is greatest number")
#         else:
#             print(b,"is greatest number")
#     else:
#         print(c,"is greatest number")
# else:
#     print(d,"is greatest number")

# OR USING HARRY'S METHOD
# use of pass

if(a>d):
    f1 = a
else:
    f1 = d

if(b>c):
    f2 = b
else:
    f2 = c

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")