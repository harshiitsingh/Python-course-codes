# Use open function to read the content of a file!

# f = open('09_01_sample.txt', 'r')  # open is built in fxn
f = open('09_01_sample.txt')  # by default the mode is r
data = f.read()
data1 = f.read(5)  # reads only first 5 characters.
print(data)
print(data1)
f.close()