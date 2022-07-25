n = int(input ("Enter number of terms you want to print: "))  
n_1 = 0
n_2 = 1
i=2
List=[n_1,n_2]
while i<n:
  fibo=n_1+n_2
  List.append(fibo)
  n_1=n_2
  n_2=fibo
  i+=1
print(List)