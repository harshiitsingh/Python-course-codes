#  Write a Python program to create a histogram from a given list of integers. 
def histogram(items):
    for n in items:
        output = ''
        times = n # what if we do not make times variable and only take n (like, n>0, n=n-1)
        while(times>0):
            output += "*"
            times = times - 1
        print(output)

histogram([2,3,6,5]) # here items = [2,3,6,6]