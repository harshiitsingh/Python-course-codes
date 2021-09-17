'''
Q.4 Write a function that accepts two positive integers a and b 
and returns a list of all the even numbers between a and b (including a and b).
'''

x = eval(input("Enter the starting integer: "))
y = eval(input("Enter the ending integer: "))
start, end = x, y

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end = " ")


# OR
# # Python program to print even Numbers in a List  
# # list of numbers
# list1 = [10, 21, 4, 45, 66, 93]
  
# # using list comprehension
# even_nos = [num for num in list1 if num % 2 == 0]
  
# print("Even numbers in the list: ", even_nos)

# OR
# def is_even_num(l):
#     enum = []
#     for n in l:
#         if n % 2 == 0:
#             enum.append(n)
#     return enum
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))