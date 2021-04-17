# Q.1 WAP using function to find greatest of three numbers.

# def maximum(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# m = maximum(3,5,9)
# print("The value of maximum is "+ str(m))

# My method
def maximum(n1,n2,n3):
    return max(n1,n2,n3)

# print(str(maximum(3,5,9)))
print(maximum(3,5,9))
            

# Q.2 WAP in python using function to convert celsius to farhenheit. 

def convert(celsius):
    return (celsius * 9/5) + 32

c = int(input("Enter the value of temperture in celsius: "))
print(convert(c))

# Q.3 How do you prevent a python print() fxn to print a new line at the end?

print("Hello,")
print("How")
print("are")
print("you?")

print("Hello,", end="") # by default end = "\n", but here we have changed it.
print("How", end="")
print("are", end="")
print("you?", end="")


print("Hello,", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?", end=" ")