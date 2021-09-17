# Write a Python program to find sum of given number in the text file “numbers.txt” using Files.

total = 0

with open('numbers.txt') as infile:
    with open('results.txt', 'w') as outfile:

        for line in infile:
            try:
                num = int(line)
                total += num
                print(num, file=outfile)
            except ValueError:
                print("'{}' is not a number".format(line.rstrip()))
                # print(f"'{line}' is not a number")

print(total)

# # MY METHOD
# with open("numbers.txt", "r") as f:
#     a = int(f.readline())
#     b = int(f.readline())
#     c = int(f.readline())

# print(a+b+c)

# # METHOD -2
# f=open("numbers.txt", "r")
# s=f.readlines()
# p=str(s)

# for line in s:
#     printnum=0
#     try:
#         printnum+=float(line)
#         print("Adding:", printnum)    
#     except ValueError:
#         print("Invalid Literal for Int() With Base 10:", ValueError)

#     for line in s: 
#         if p.isdigit():
#         total=0            
#             for number in s:    
#                 total+=int(number)
#                 print("The sum is:", total)

# # METHOD - 3
# total = 0

# with open('numbers.txt', 'r') as inp, open('output.txt', 'w') as outp:
#    for line in inp:
#        try:
#            num = float(line)
#            total += num
#            outp.write(line)
#        except ValueError:
#            print('{} is not a number!'.format(line))

# print('Total of all numbers: {}'.format(total))

