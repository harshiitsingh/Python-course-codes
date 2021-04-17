from decimal import *

# GRAVITATIONAL_CONSTANT = Decimal('6.67384E-11')
G=6.673*(10**-11)
mass = float(input("Enter mass of planet:"))
radius = float(input("Enter radius of planet:"))

def escape_velocity(mass, radius):
    '''Calculates the delta-V escape velocity.

    Returns delta-V in meters per second for the escape
    velocity for a given object given its mass in kilograms
    and its radius in meters.'''

    if mass == Decimal('0') or radius == Decimal('0'):
        # User gave a mass or radius which is unrealistic,
        # abort.
        return None
    
    result = Decimal((2 * G * mass) / radius)
    result = result.sqrt()

    return result


print("The escape velocity of planet is:",escape_velocity(mass,radius),"m/sec")
