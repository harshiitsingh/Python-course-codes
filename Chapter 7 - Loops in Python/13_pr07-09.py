# Q.7 WAP to print the following star pattern (for n = 3)
n = 3
for i in range(3):
    # for j1 in range(n-i-1):
    print(" " * (n-i-1), end = "") # by using end it will not print new line
    print("*" * (2*i+1), end = "")
    print(" " * (n-i-1))


# Q.8 WAP to print the following star pattern (for n = 3)

n = 4

for i in range(4):
    print("* " * (i+1))
    # print("*" * (i+1))
    # print("*" * i)

# Q.9 WAP to print the following star pattern (for n = 3)