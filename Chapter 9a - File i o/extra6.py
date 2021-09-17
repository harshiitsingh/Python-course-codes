'''
6. Create a file numbers.txt with numbers stored in it. Write a program to read the file, 
check for odd and even numbers and 
write the odd and even numbers separately in two files namely odd.txt and even.txt
'''

with open('numbers1.txt', 'r') as f:
    f1 = open('odd.txt', 'w')
    f2 = open('even.txt', 'w')
    for line in f:
        try:
            num = int(line)
            if (num %2 != 0):
                print(num, file=f1)
            else:
                print(num, file=f2)
        except ValueError:
            print("'{}' is not a number".format(line.rstrip()))