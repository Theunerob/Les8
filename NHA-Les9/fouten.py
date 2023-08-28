import math

def discriminant(a,b,c):
    D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
    D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
    uitvoer = list[D1,D2]
    return(uitvoer)

print(discriminant(4,3,3))