# Q.10 WAP to print multiplication table of n using for loop in reversed order.

num = int(input("Enter the number: "))

for i in range(11,0):
    # print(str(num) + " X " + str(i) + " = " + str(i*num))
    # use of f strings
    print(f"{num}X{i}={num*i}")
