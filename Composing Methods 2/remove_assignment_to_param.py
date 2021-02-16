# By Kami Bigdely
# Remove assignment to method parameter.
"""This file will calculates kinnetic energy"""

class Distance:
    """Represents the distance"""
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

class Mass:
    """Represents the mass of the object"""
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def calculate_kinetic_energy(object_mass, dist, time):
    """This method will calculate the kinetic energy"""
    if dist.unit != 'km':
        # [ly] stands for light-year (measure of distance in astronomy)
        if dist.unit == "ly":
            # convert from light-year to km unit
            in_km = dist.value * 9.461e12
            dist = Distance(in_km, "km")
        else:
            print("unit is Unknown")
    speed = distance.value/time  # [km per sec]
    if object_mass.unit != 'kg':
        if object_mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = object_mass.value * 1.98892e30  # [kg]
            object_mass = Mass(value, 'kg')
        else:
            print("unit is Unknown")

    kinetic_energy = 0.5 * mass.value * speed ** 2
    return kinetic_energy


mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
