a = {1,2,3}
b = {2,1,3}
if a == b:
    print("yes")


n = int(input("Enter a number: "))
 
fac = 1
i = 1
 
while i <= n:
	fac = fac * i
	i = i + 1
 
print("Factorial of", n, "is", fac)

n = int(input("Enter a number:"))
total =0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print("The total sum of digits is:",total)

n = int(input("Enter a number: "))
def checkEvenOdd(n):
    
    if(n%2==0):
        print(n,"is an even")
    else:
        print(n,"is an odd")

checkEvenOdd(n)