__author__ = 'bglasser'
from bitarray import bitarray
prime = 2
rng = 2**20
numLine = bitarray(rng)
numLine.setall(True)
numLine[1] = False
def getNextPrime():
    global prime
    numLine[:-1:prime] = False
    prime = numLine.index(True)

for i in range(10000):
    print "%s: %s"%(i,prime)
    getNextPrime()

print prime


#>>> a[11:37:3] = 9 * bitarray([True])
#>>> a
#bitarray('00000000000100100100100100100100100100000000000000')