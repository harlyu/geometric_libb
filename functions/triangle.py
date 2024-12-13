import math

def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")
    p= (a + b + c) / 2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")
    return a + b + c
