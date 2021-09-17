# Q.2 Create a class pets from the class Animals and further create 
# class Dog from Pets. Add a method bark to class Dog.

class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()