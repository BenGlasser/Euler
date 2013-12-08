__author__ = 'bglasser'
from problem003 import __init__ as prime

def testPrime():
    for i in range(50):
        if prime.isPrime(i):
            print"%s is Prime"%(i)
        else:
            print"%s is NOT Prime"%(i)

if __name__ == '__main__':
    testPrime()