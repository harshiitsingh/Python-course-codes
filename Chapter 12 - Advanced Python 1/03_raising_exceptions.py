
def increment(num):
    try:
        return int(num) + 1
    except:
        # raise ValueError("This is not good - Harshit")
        print("Value Error")

a = increment(34)
b = increment('3dd4')
print(a)
print(b)