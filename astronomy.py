# DON'T DO ANYTHING IN THIS PROGRAM UNLESS YOU KNOW WHAT YOUR DOING :)
# THIS PROGRAM IS FOR EDUCATIONAL PURPOSEs ONLY YOU CAN CHANGE ANY VALUE IN THIS PROGRAM BUT MAKE SURE YOU DO I CORRRECTLY :)

# CREDIT: MARK JOHN A. VELMONTE


import math

#constant
gravConstant = 6.67408e-11 #kg
speedOfLight = 299792458 #m/s

#variables

#mercury
mercury_mass = 3.3011e+23 #kg
mercury_aphelion= 0.466697 #au
mercury_perihelion = 0.307499 #au
mercury_semiMajorAxis = 0.387098 #au
mercury_eccentricity = 0.205630 #au
mercury_orbitalPeriod = 87.9691 #days
mercury_synodicPeriod = 115.88 #days
mercury_AveOrbitalSpeed = 47.362 #km/s
mercury_meanAnomaly = 174.796 #degress
mercury_elipticInclinitaiion = 7.005 #degrees
mercury_sunEquatorInclination = 3.38 #degrees
mercury_invariablePlaneInclination = 6.34 #deegress
mercury_longitudeAsNode = 48.331 #degrees
mercury_argPerihelion = 29.124 #degrees
mercury_sattelites = 0
mercury_meanRadius = 2439.7 #km

#venus
venus_mass = 4.8675e+24  #kg
venus_aphelion= 0.728213 #au
venus_perihelion = 0.718440 #au
venus_semiMajorAxis = 0.723332 #au
venus_eccentricity = 0.006772 #au
venus_orbitalPeriod = 224.701 #days
venus_synodicPeriod = 583.92 #days
venus_AveOrbitalSpeed = 35.02 #km/s
venus_meanAnomaly = 50.115 #degress
venus_elipticInclinitaiion = 3.39458 #degrees
venus_sunEquatorInclination = 3.86 #degrees
venus_invariablePlaneInclination = 2.19 #deegress
venus_longitudeAsNode = 76.680 #degrees
venus_argPerihelion = 54.884 #degrees
venus_sattelites = 0
venus_meanRadius = 6051.8 #km

#earth
  #no longitude ascending node 
earth_mass = 5.97237e+24 #kg
earth_aphelion= 1.017 #au
earth_perihelion = 0.983 #au
earth_semiMajorAxis = 1.00000102 #au
earth_eccentricity = 0.0167086 #au
earth_orbitalPeriod = 365.256363004 #days
earth_AveOrbitalSpeed = 29.78 #km/s
earth_meanAnomaly = 358.617 #degress
earth_elipticInclinitaiion = 0.00005 #degrees
earth_sunEquatorInclination = 7.155 #degrees
earth_invariablePlaneInclination = 1.57869 #deegress
earth_argPerihelion = 114.20783 #degrees
earth_sattelites = 1
earth_meanRadius = 6371.0 #km

#mars
mars_mass = 6.4171e+23 #kg
mars_aphelion= 1.666 #au
mars_perihelion = 1.382 #au
mars_semiMajorAxis = 1.523679 #au
mars_eccentricity = 0.0934 #au
mars_orbitalPeriod = 686.971 #days
mars_synodicPeriod = 779.96 #days
mars_AveOrbitalSpeed = 24.007 #km/s
mars_meanAnomaly = 0.52407109 #degress
mars_elipticInclinitaiion = 1.850 #degrees
mars_sunEquatorInclination = 5.65 #degrees
mars_invariablePlaneInclination = 1.67 #deegress
mars_longitudeAsNode = 1.85061 #degrees
mars_argPerihelion = 286.502 #degrees
mars_sattelites = 2
mars_meanRadius= 3389.5 #km


# equations

def eccentricity(a, p):
    e = (a - p) / (a + p)
    return e

def aphelion(a, e):
    Ra = a * (1 + e)
    return Ra

def perihelion(a, e):
    Rp = a * (1 - e)
    return Rp

def orbitalPeriod(i):
    orbPer = math.sqrt(i**3)
    return orbPer

def schRad(m):
    R = (2 * gravConstant * m) / (speedOfLight**2)
    return R