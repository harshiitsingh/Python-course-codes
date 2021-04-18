# dunder methods
class Number:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,num2):
        print("Lets add")
        # return 300
        return self.num + num2.num

    def __mul__(self,num2):
        print("Lets multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
# n1 + n2
sum = n1 + n2
print(sum)
mul = n1 * n2
print(mul)

# python docs for operator overloading