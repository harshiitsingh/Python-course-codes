n = int(input ("Enter number of terms you want to print: "))  
  
# First two terms  
n_1 = 0  
n_2 = 1  
count = 0  

if n <= 0:  
    print ("Invalid Number!")  

elif n == 1:  
    print ("The Fibonacci sequence of the numbers up to", n, ": ")  
    print(n_1)  

else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n:  
        print(n_1, end=" ")  
        nth = n_1 + n_2  
        # At last, we will update values  
        n_1 = n_2  
        n_2 = nth  
        count += 1  