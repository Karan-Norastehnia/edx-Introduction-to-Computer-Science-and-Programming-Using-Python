from math import pi
from math import tan

def polysum(n, s):
    area      = (1/4 * n * (s**2)) / (tan(pi/n))
    perimeter = (n * s)**2

    return round(area, 4) + round(perimeter, 4)