n=int(input("Enter the number of rows: "))
for i in range(n):
   for j in range(i+1,-0,-1):
       print(j%2,end=" ")
   print()

