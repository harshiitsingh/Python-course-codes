# Write a program to check whether a given string is a palindrome or not.

str = input("Enter string: ")

if(str==str[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")