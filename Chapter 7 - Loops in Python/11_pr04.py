# Q.4 WAP to find whether a given is prime or not.

num = int(input("Enter the number: "))
prime = True
for i in range(2,num):
    if(num%i == 0): # or if(num%i == 0 and num != 2):
        prime = False
        break

if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")

# Q.5 WAP to find the sum of first n natural numbers using while loop.

n = int(input("Enter the end number: "))
s = 0
i = 0
while i<=n:
    s = s+i
    i = i+1

print(s)