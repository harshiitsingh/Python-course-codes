# Global keyword

a = 54 # global variable
def func1():
    global a
    print(f"Print statment 1: {a}")
    a = 6 # local variable.... if global keyword is not used
    print(f"Print statment 2: {a}")

func1()
print(f"Print statment 3: {a}")