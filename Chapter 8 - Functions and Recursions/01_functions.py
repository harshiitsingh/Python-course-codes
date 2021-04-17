marks = [45, 78, 86, 77]
average = sum(marks)/4       # or average = (marks[0] + marks[1] + marks[2] + marks[3])/4
percentage = (sum(marks)/400)*100
print(percentage)

marks2 = [75, 88, 96, 78]
percentage2 = (sum(marks2)/400)*100
print(percentage2)

# OR 
def percent(marks):
    return (sum(marks)/400)*100  # only for 4 subjects

marks1 = [64,70,77,86]
percentage = percent(marks1)
print(percentage)
# or
print(percent(marks1))

# QUICK QUIZ - WAP to greet a user with "Good day" using functions.