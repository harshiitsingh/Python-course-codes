# Q.2 Write a program to greet all the person names stored in a list l1 and which start with S.

l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello",name) # or print("Hello " + name)

# attemt above problem using while loop.