def greet(name):
    print("Good day, "+ name)

greet("Harry")
# greet()   # --> this will throw an error

# NOW

def greet(name="Stranger"):
    print("Good day, "+ name)
greet("Harry")
greet()