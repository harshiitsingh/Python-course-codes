class Number:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,num2):
        print("Lets add")

n1 = Number(4)
n2 = Number(6)
n1 + n2
