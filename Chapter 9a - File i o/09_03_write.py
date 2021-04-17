
f = open('another.txt', 'w')
f.write("Please2 write this to the file")
f.write("I am appending")
f.close()

f = open('another.txt', 'a')
# f.write("Please2 write this to the file")
f.write("I am appending")
f.close()