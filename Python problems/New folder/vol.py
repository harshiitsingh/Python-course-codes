import math

radius = eval(input("Enter the radius of sphere: "))

Volume = 4/3 * math.pi * pow(radius, 3)
print("Volume of the Sphere =", Volume)

SurfaceArea = 4 * (math.pi) * (radius*radius)  
print("Surface area of the sphere =", SurfaceArea)  
