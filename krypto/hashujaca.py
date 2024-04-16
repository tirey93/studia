import math
import random

import sympy
from Crypto.Hash import MD5
from sympy import randprime

e = pow(2, 16) + 1
def nwd(e, fi):
    return math.gcd(e, fi)
def findModInv(e, fi):
    return pow(e, -1, fi)

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

#NADAWCA
p = sympy.randprime(2**128,2**129)
q = sympy.randprime(2**128,2**129)


n = getPublicKey(p, q)
d = getPrivateKey(p, q)

wiad = "moja wiadomosc"
H = MD5.new()
H.update(bytes(wiad, 'UTF-8'))
hash = H.hexdigest()
print(f"nadawca hash: {hash}")
hash_int = int.from_bytes(bytes(hash, 'UTF-8'))
print(f"nadawca hash_int: {hash_int}")
podpis = pow(hash_int, d, n)

#ODBIORCA(dostaje podpis i wiad, n)
hash_odbiorcy_int = pow(podpis, e, n)
print(f"odbiorca hash_int: {hash_odbiorcy_int}")
hash_odbiorcy = hash_odbiorcy_int.to_bytes(32,'big').decode("UTF-8")
print(f"hash odbiorcy: {hash_odbiorcy}")
print(hash_odbiorcy == hash)