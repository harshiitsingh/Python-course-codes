'''
Q.9 Write a program to check whether the list is a palindrome or not using function
'''
list = []
n = int(input("Enter the number of elements for the list: "))

for i in range(0,n):
    list.append(input(f"Enter element [{i + 1}] in a list: "))

if list == list[::-1]:
    print("The list is a palindrome")
else:
      print("The list isn't a palindrome")