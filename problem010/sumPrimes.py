__author__ = 'bglasser'

from bitarray import bitarray
prime = 2
rng = 2000000
numLine = bitarray(rng)
numLine.setall(True)
numLine[1] = False
sum = 0
prev = -1

def getNextPrime():
    global prime
    numLine[:-1:prime] = False
    prime = numLine.index(True)

while prev != prime:
    sum += prime
    getNextPrime()
    print "%s: %s"%(prime, sum)

print sum