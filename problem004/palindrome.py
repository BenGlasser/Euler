__author__ = 'bglasser'
from datetime import datetime

largest = 999 * 999

def reverse(str):
    if str.__len__() == 0: return ""
    return str[-1] + reverse(str[0:-1])

def isPalendrome(num):
    numStr = num.__str__()
    length = numStr.__len__()
    range = length/2
    front = numStr[0:range]
    if length % 2 == 0:
        back = reverse(numStr[range:length])
    else:
        back = reverse(numStr[range+1:length])
    print "%s = %s"%(front, back)
    return front == back

def getNext():
    global largest
    while largest > 0:
        largest -= 1
        if isPalendrome(largest):
            return largest

def factor(num):
    for i in range(100,999):
        if num%i == 0 and (num/i).__str__().__len__() == 3:
            return [i, num/i]
    return None

def findPalendrome():
    while largest > 0:
        num = factor(getNext())
        if num is not None:
            return "%d = %d x %d" % (largest, num[0], num[1])

start = datetime.now()
print findPalendrome()
print "finished search in %s" % (datetime.now()-start)