import math

def discriminant(a,b,c):
    D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
    D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)  

    uitvoer = list[D1,D2]
    return(uitvoer)

A = int(input("Geef waarde A"))
B = int(input("Geef waarde B"))
C = int(input("Geef waarde C"))

# print(type(A1))

uitkomst = discriminant(A,B,C)

print(uitkomst)

D1 = uitkomst[0]
D2 = uitkomst[1]

print(f"De discriminant(en) voor {a}x^2 + {b}x + {c} zijn :")
print(f"{D1} en {D2}")