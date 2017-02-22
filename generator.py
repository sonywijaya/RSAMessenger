import random
from fractions import gcd

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
      if n%f == 0: return False
      if n%(f+2) == 0: return False
      f +=6
    return True

def coPrime(a, b):
    if (gcd(a, b) != 1):
        return False
    else:
        return True

def getPrime():
    primes = [i for i in range(0,500) if isPrime(i)]
    key = random.sample(primes, 2)
    return key

def getE(n, z):
    coprimes = []
    for i in range(n)[2:]:
        if (coPrime(i, n) and coPrime(i, z)):
            coprimes.append(i)
    e = coprimes[0]
    return e
    
def getD(z, e):
    for i in range(10000000)[1:]:
        if ((((i*e) % z) == 1) and (i != e)):
            d = i
            break
    return d
