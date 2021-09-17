'''
Q.8 Write a Python program to get the largest number from a list
without using library Function
'''
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

# OR
# list1 = [10, 20, 4, 45, 99]
  
  
# # printing the maximum element
# print("Largest element is:", max(list1))

# # OR
# # Method 3 : Find max list element on inputs provided by user
# # Python program to find largest
# # number in a list
  
# # creating empty list
# list1 = []
  
# # asking number of elements to put in list
# num = int(input("Enter number of elements in list: "))
  
# # iterating till num to append elements in list
# for i in range(1, num + 1):
#     ele = int(input("Enter elements: "))
#     list1.append(ele)
      
# # print maximum element
# print("Largest element is:", max(list1))