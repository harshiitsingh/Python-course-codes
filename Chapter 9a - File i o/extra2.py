'''
2. Write a Program to read the contents of mark.txt. Calculate the total marks and
percentage by each student. Use readline().split() . First line in the file contains the total
number of students
'''

with open('marks.txt', 'r') as f:
    print("Total no. of students are:",f.readline())
    
    s = [1,2,3,4,5]
    for i in s:
        total = 0
        for i in f.readline().split():
            i = int(i)
            total += i
        print(f"Total marks of student is {total} and his percentage is {(total/500)*100}")