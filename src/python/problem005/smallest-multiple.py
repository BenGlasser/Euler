__author__ = 'bglasser'

from datetime import datetime

#first run finished search in 0:00:48.415316

def div(num):
    return num%20 == 0 and \
           num%19==0 and \
           num%18==0 and \
           num%17==0 and \
           num%16==0 and \
           num%15==0 and \
           num%14==0 and \
           num%13==0 and \
           num%12==0 and \
           num%11==0 and \
           num%10==0 and \
           num%9==0 and \
           num%8==0 and \
           num%7==0 and \
           num%6==0 and \
           num%5==0 and \
           num%4==0 and \
           num%3==0 and \
           num%2==0 and \
           num%1==0

def findMult():
    num = 0
    while True:
        num+=20
        print "testing: %d" % (num)
        if div(num):
            return num

start = datetime.now()
print findMult()
print "finished search in %s" % (datetime.now()-start)
