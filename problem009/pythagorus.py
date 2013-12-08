__author__ = 'bglasser'
import math
rng = 1000

def searchTriplet():
    for a in range(1,rng):
        for b in  range(1,rng):
            if testTriplet(a, b):
                print "%s * %s * %s = %s"%(a, b, int(math.sqrt(a**2 + b**2)), a*b*int(math.sqrt(a**2 + b**2)))
                return

def testTriplet(a, b):
    c = math.sqrt(a**2 + b**2)
    if (c%1 == 0):
        return a + b + c == 1000
    return False

searchTriplet()
