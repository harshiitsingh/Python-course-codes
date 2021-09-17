'''
Q.5 Write a class vector representing a vector of n dimensions.
Overload the + and * operator which calculates the sum and the dot 
product of them.
'''

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]
    
    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] + vec2.vec[i]
        return sum

v1 = Vector([1, 4, 6, 6, 32, 23])
print(v1)
v2 = Vector([1, 4]) # Vector([1, 4, 6]) 
v3 = Vector([1, 6]) # Vector([1, 6, 9]) 
print(v2 + v3)
print(v2 * v3) # a scalar quantity
