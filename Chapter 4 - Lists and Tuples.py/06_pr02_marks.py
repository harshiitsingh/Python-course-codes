m1 = int(input("Enter marks for student number 1: "))
m2 = int(input("Enter marks for student number 2: ")) 
m3 = int(input("Enter marks for student number 3: "))
m4 = int(input("Enter marks for student number 4: "))
m5 = int(input("Enter marks for student number 5: "))
m6 = int(input("Enter marks for student number 6: ")) 
m7 = int(input("Enter marks for student number 7: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)

# Q.4 Write a program to print sum of element of a list
a = [2,4,56,7]
print(a[0] + a[1] + a[2] + a[3]) # not best way to add, use loops ,it will be easy. OR
print(sum(a))