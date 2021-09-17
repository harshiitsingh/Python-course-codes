'''
1.	If ATM contains Indian currency notes of 100, 500, and 2000. To withdraw cash from ATM, the user has to enter number of notes he/she wants of each currency i.e. of 100, 500 and 2000. So write a program calculate total amount withdrawn by person from ATM in terms of rupees.  (45 marks)

Sample Output: 

Enter the number of 100Rs notes you want to withdraw:5 
Enter the number of 500Rs notes you want to withdraw:5 
Enter the number of 2000Rs notes you want to withdraw:4 
Total Amount Withdrawn = 1100 Rs 
'''

oneHundreds = int(input("Enter the number of 100Rs notes you want to withdraw: "))
fiveHundreds = int(input("Enter the number of 500Rs notes you want to withdraw: "))
twoThousands = int(input("Enter the number of 2000Rs notes you want to withdraw: "))

totalAmount = (oneHundreds*100) + (fiveHundreds*500) + (twoThousands*2000)
print("Total Amount Withdrawn =", totalAmount, "Rs")