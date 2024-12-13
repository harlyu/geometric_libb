import math


def area(r):
    if r <= 0:
        raise ValueError("Radius must be a positive number.")
    return math.pi * r * r

def perimeter(r):
    if r <= 0:
        raise ValueError("Radius must be a positive number.")
    return 2 * math.pi * r
