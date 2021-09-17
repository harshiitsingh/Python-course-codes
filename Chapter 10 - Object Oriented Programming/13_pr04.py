# Add a static method in Problem 2 to greet the user with hello

class Calculator:
    def __init__(self, num):
        self.number = num # num is a variable which is given to the fxn but number is an argument and will set the number of the instance given

    def square(self):
        print(f"The value of {self.number} square is {self.number ** 2}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number ** 3}")

    def squareRoot(self):
        print(f"The value of {self.number} squareroot is {self.number ** 0.5}")

    @staticmethod
    def greet():
        print("*****Hello there welcome to the best calculator of the world*****")

a = Calculator(9)
a.greet()
a.square()
a.squareRoot()
a.cube()