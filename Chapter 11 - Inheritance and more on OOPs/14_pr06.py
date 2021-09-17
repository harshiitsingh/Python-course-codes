'''
Write __str__() method to print the vector as follows:
        7i + 8j + 10k
Assume vector of dimension 3 for this problem.
'''

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1)
print(v2)
