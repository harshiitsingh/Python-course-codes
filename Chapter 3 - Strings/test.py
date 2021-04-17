# Calculating Escape velocity of a planet 

# Escape velocity, V = sqrt(2GM/r)

G = 6.673 * (10 ** -11)  #Gravitational Constant

mass = float(input("Enter the mass of the planet (in Kg) : "))
    
r = float(input("Enter the radius of the planet (in metre) : "))

def escape_velocity():
    
    V = (2*G*mass)/r
    Ve = V ** 0.5 

    print("The Escape Velocity of the planet is: ", Ve, "m/sec")

if __name__=='__main__':
    escape_velocity()
else:
    print("Enter appropriate details")

'''
for example, in case of Earth
mass = 5972000000000000000000000 Kg
r(radius of Earth) = 6371000 m
hence, escape velocity is, Ve = 11186 m/s (approx)
'''