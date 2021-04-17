# Q.6 WAP to calculate the factorial of a given number using for loop.
num = int(input("Enter the number: "))
factorial = 1
# fact = 0
for i in range(1,num+1):
    factorial = factorial * i
    # fact = fact + factorial

# print(fact)
print(f"The factorial of {num} number is {factorial}")