import math
import time

#constant value
grav = 6.67*10**-11
c = 299792458


commands = "LIST() orbit() orbitalPeriod() sch() ecc() dontUseThisCode()".split(" ")

print("wrong input can lead to sintax error")
print(" commands below ")

for i in commands:
    print(i)

def LIST():
    print("list of commands:")
    for i in commands:
        print(i)

def orbit():
    print("calculate object aphelion and perihelion")
    a = float(input("enter the planet distance from sun in au >>> "))
    e = float(input("enter the palnet eccentricity >>> "))

    def aphelion(a, e):
        total = a*(1 + e)
        print("planet perehilion is >>> " + str(total) + "au")
        
    def perihelion(a, e):
        total = a*(1 - e)
        print("planet perihelion is >>> " + str(total) + "au")

    aphelion(a, e)
    perihelion(a, e)


def orbitalPeriod():
    print("calculate the orbital period of the object")
    a = input(" enter the object distance from the sun in au >>> ")
    total = (math.sqrt(float(a)**3))*365.25
    print(total)

def dontUseThisCode():
    tminus = 3
    while tminus >= 1:
        time.sleep(1)
        tminus -= 1
        print(tminus)
        if tminus == 0:
            print("wwuuuvvvv yaaaaaahh <3 :)")

def sch():
    print("calculate swarztchild blackhole gravity")
    m = float(input("enter planet mass in km ex(9.972) without the x10 >>> "))
    n = int(input("second parameter >>> "))
    o = m*10**n
    op1 = (2 * grav * o)
    op2 = op1 / c**2
    total = op2
    print(total)

def ecc():
    print("calculate the eccentricity of an object in parent star")
    aph = float(input("input object aphelion >>> "))
    per = float(input("input object perehilion >>> "))
    opr1 = aph - per
    opr2 = aph + per
    opr3 = opr1 / opr2
    total = opr3

    print("the object eccentricity is " + str(total))