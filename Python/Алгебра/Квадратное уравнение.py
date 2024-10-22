from math import sqrt

def quadratic_equation(a, b, c):
    discr = b**2 - 4*a*c
    x1 = (-b + sqrt(discr)) / 2*a
    x2 = (-b - sqrt(discr)) / 2*a
    return (x1, x2)

print(quadratic_equation(1, 10, -3))