# write a python program to search a number using binary searching.

list = []
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    element = int(input())
    list.append(element) # adding the element
     
print("List :", list)

def binary_search(list, element):
	first = 0
	last = len(list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if list[mid] == element :
			found = True
		else:
			if element < list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

element = int(input("Enter the element you want to search :"))

result = binary_search(list, element)
# print(binary_search([1,2,3,5,8], 6))
# print(binary_search([1,2,3,5,8], 5))

# def binary_search(list1, n):  
#     low = 0  
#     high = len(list1) - 1  
#     mid = 0  
  
#     while low <= high:  
#         # for get integer result   
#         mid = (high + low) // 2  
  
#         # Check if n is present at mid   
#         if list1[mid] < n:  
#             low = mid + 1  
  
#         # If n is greater, compare to the right of mid   
#         elif list1[mid] > n:  
#             high = mid - 1  
  
#         # If n is smaller, compared to the left of mid  
#         else:  
#             return mid  
  
#             # element was not present in the list, return -1  
#     return -1  
  
  
# # Initial list1  
# list1 = [12, 24, 32, 39, 45, 50, 54]  
# n = 45  
  
# # Function call   
# result = binary_search(list1, n)  
  
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1")  


	https://www.google.com/search?q=how+to+insert+a+list+using+user+in+python&rlz=1C1CHBF_enIN965IN965&oq=how+to+insert+a+list+using+user+in+python&aqs=chrome..69i57.11828j0j1&sourceid=chrome&ie=UTF-8