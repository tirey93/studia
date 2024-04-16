from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from sympy import randprime

W = b'cos'
KL = get_random_bytes(16)
CIPHER = AES.new(KL, AES.MODE_ECB)
KRYPTO = CIPHER.encrypt(pad(W, 16))
W2 = CIPHER.decrypt(KRYPTO)
# print(W2)


# ODBIORCA
p = randprime(2**128, 2**129)
q = randprime(2**128, 2**129)
n = p*q
fi = (p - 1)*(q - 1)
e = 2**16 + 1
d = pow(e, -1, fi)

#NADAWCA - dostaje (e,n)
W = b'cos'
KL = get_random_bytes(32)
# print(f"KL: {KL}")
CIPHER = AES.new(KL, AES.MODE_EAX)
nonce = CIPHER.nonce
KRYPTO = CIPHER.encrypt(pad(W, 16))

KL_TAJNY = pow(int.from_bytes(KL), e, n)

#ODBIORCA dostaje (KL_TAJNY, KRYPTO)
KLUCZ_2 = pow(KL_TAJNY, d, n).to_bytes(32, 'big')
# print(f"KLUCZ_2: {KLUCZ_2}")
CIPHER2 = AES.new(KLUCZ_2, AES.MODE_EAX, nonce=nonce)
W3 = CIPHER2.decrypt(KRYPTO)
print(f"odp: {unpad(W3, 16)}")














