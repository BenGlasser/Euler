__author__ = 'bglasser'
import math
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

def isPrime(int):
    for i in range(2,math.ceil(math.sqrt(int)).__int__()):
        if int % i == 0:
            return False
    return True

def largestPrime(int):
    div = start = math.ceil(math.sqrt(int)).__int__()
    for i in range(start):
        if isPrime(div) and int%div == 0:
            return "Largest prime divisor for %d is %d"%(int, div)
        div-=1
        print "tested: %d"%(div)

print largestPrime(13195)
print largestPrime(600851475143)