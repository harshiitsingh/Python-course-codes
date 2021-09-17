# Write a program to read the numbers from a file and count the number of even and odd Numbers
countEven = 0
countOdd = 0

with open('evenodd.txt') as f:
    for line in f:
        try:
            num = int(line)
            if (num %2 == 0):
                countEven += 1
            else:
                countOdd +=1
        except ValueError:
            print("'{}' is not a number".format(line.rstrip()))

print("Total even numbers in the file are",countEven)
print("Total odd numbers in the file are",countOdd)

# def counteven(filename):
#   countOfEvenNumbers = 0
#   infile = open(filename, 'r')
#   for line in infile:
#     number = int(line)
#     if (number %2 == 0):
#       countOfEvenNumbers+= 1
#   infile.close()
#   return countOfEvenNumbers



# method 3
# def counteven(integers):
#     return sum(1 for n in integers if n % 2 == 0)

# with open('evenodd.txt') as f:
#     numbers = (int(line) for line in f)
#     print(counteven(numbers))
