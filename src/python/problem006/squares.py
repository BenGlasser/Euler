__author__ = 'bglasser'


def sumOfSquares(num):
    result = 0
    for i in range(1,num+1):
        print "%s + " % (i**2)
        result += i**2
    return result

def squareOfSum(num):
    result = 0
    for i in range(1,num+1):
        result += i
    return result**2

square = squareOfSum(100)
sum = sumOfSquares(100)
print "%s - %s = %s"% (square, sum, square - sum)