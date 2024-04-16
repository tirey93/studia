import random
import math

e = pow(2, 16) + 1
def nwd(e, fi):
    return math.gcd(e, fi)
def findModInv(e, fi):
    for x1 in range(fi):
        if (e * x1) % fi == 1:
            return x1
def findPrimeNumber(min, max, exceptNumber = None):
    number = random.randint(min, max)
    if number % 2 == 0 or number == exceptNumber:
        number += 1
    while not isPrimeNumber(number):
        number += 2
    return number

def isPrimeNumber(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def tryFindPrivateKey(p, q):
    try:
        n = getPrivateKey(p, q)
    except:
        n = tryFindPrivateKey(p, q)
    return n
def getPublicKey(p, q):
    return p*q
def getPrivateKey(p, q):
    fi = (p - 1) * (q - 1)

    if nwd(e, fi) != 1:
        raise Exception("GCD not found")

    # print(f"e: {e}, fi: {fi}")
    return findModInv(e, fi)

p = findPrimeNumber(256,512)
q = findPrimeNumber(256,512, p)


n = getPublicKey(p, q)
d = getPrivateKey(p, q)

#pow(e, -1, fi)
x = 1000
print(f"x: {x}")
y = (pow(x, e)) % n
print(f"y: {y}")

xAgain = (pow(y, d)) % n
print(f"xAgain: {xAgain}")


