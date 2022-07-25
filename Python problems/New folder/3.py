import math

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

discriminant = (b * b) - (4 * a * c)

# If discriminant is positive
if discriminant>0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    print(f"Two distinct and real roots exists: {root1} and {root2}")

# If discriminant is not positive
else:
    # If discriminant is negative 
    if discriminant<0:
        root1 = root2 = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * a)

        print(f"Two distinct complex roots exists: {root1} + i{imaginary} and {root2} - i{imaginary}")

    # If discriminant is zero 
    else:
        root1 = root2 = -b / (2 * a);

        print(f"Two equal and real roots exists: {root1} and {root2}")