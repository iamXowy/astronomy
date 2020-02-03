import math

print("wrong input can lead to sintax error")
a = float(input("enter the planet distance from sun in au >>> "))
e = float(input("enter the palnet eccentricity >>> "))

def aphelion(a, e):
    total = a*(1 + e)
    print("planet aphelion is " + str(total) + "au")

def perihelion(a, e):
    total = a*(1 - e)
    print("planet perihelion is " + str(total) + "au")

aphelion(a, e)
perihelion(a, e)

