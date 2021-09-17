'''
Q.7 Write a function assign_grade(list1) which reads the marks of a student from a list and
assigns a grade based on the following conditions:

if marks>=90 then grade A

if marks>=80 && <90 then grade B

if marks>=65 && <80 then grade C

if marks>=40 && <65 then grade D

if marks<40 then grade F
'''
# Q.7
def assign_grade(list):
    for i in range(0,len(list)):
        if list[i]>=90:
            print("Grade for",list[i],"is Grade A")
        elif list[i]>=80 and list[i]<90:
            print("Grade for",list[i],"is Grade B")
        elif list[i]>=65 and list[i]<80:
            print("Grade for",list[i],"is Grade C")
        elif list[i]>=40 and list[i]<65:
            print("Grade for",list[i],"is Grade D")
        else:
            print("Grade for",list[i],"is Grade F")

n = int(input("Enter the number of marks to be entered: "))
print("Enter the marks one by one: ")
list1 = []
for i in range(n):
    e = int(input())
    list1.append(e)
print("Your marks are:",list1)
assign_grade(list1)