l = ['k','c','t']
print(len(l))

val = "3/6"
print("val")

str1 = "Application"
str2=str1.replace('a','A')
print(str2)

str1 = "poWer"
str1.upper()
print(str1)

print([ord(ch) for ch in 'abc'])

t = 32.00
# [round((x-32)*5/9) for x in t]  # --> error
# print([round((x-32)*5/9) for x in t])  # --> error

set1 = set((0,9,0))
set2 = set([0,2,9])
set3 = {}
print(type(set1))
print(type(set2))
print(type(set3))

list1 = [1,3,4,2]
x = list1.pop(2)
print(x)
print(list1)
print(set([x]))
print(type(set([x])))