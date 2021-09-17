# Create a class programmer for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        # print(f"The name of the programmer is \
        #      {self.name} and the product is {self.product}")
        
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


harry = Programmer("Harry", "Skype")
harshit = Programmer("Harshit", "GitHub")
harry.getInfo()
harshit.getInfo()