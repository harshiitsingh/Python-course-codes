# Write a class calculator capable of finding square, cube and squareroot of a number.

class Calculator:
    def __init__(self, num):
        self.number = num # num is a variable which is given to the fxn but number is an argument and will set the number of the instance given

    def square(self):
        print(f"The value of {self.number} square is {self.number ** 2}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number ** 3}")

    def squareRoot(self):
        print(f"The value of {self.number} squareroot is {self.number ** 0.5}")

a = Calculator(9)
a.square()
a.squareRoot()
a.cube()