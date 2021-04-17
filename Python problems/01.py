'''
Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''
l = [60,5,4,2,17,20,8]

i = eval(input("Enter a number : "))
if i in l:
    a = True
else:
    a = False

print(a)

# or
# def is_group_member(group_data, n):
#     for value in group_data:
#         if n == value:
#             return True
#     return False
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))
  