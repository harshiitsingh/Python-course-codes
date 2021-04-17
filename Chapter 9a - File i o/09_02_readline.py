f = open('09_01_sample.txt')
data = f.readline() # read and prints only the first line.
print(data) 
data = f.readline()  # read and prints only the second line.
print(data)  # it will print /n from the text file

data = f.readline()  # read and prints only the 3rd line.
print(data)

data = f.readline()  # read and prints only the 4th line.
print(data)
f.close()

'''
Modes of opening a file :-
r -->
w -->
a -->
+ -->

'rb'
'rt'
'''