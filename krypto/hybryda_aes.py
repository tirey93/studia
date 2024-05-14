from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from sympy import randprime

W = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ac urna mattis, pulvinar felis eget, cursus purus. Vivamus nec gravida massa. Sed id purus ultricies, eleifend neque id, sagittis mauris. Phasellus ac lectus urna. Nulla mauris arcu, posuere sit amet euismod sit amet, semper in arcu. Curabitur vel augue vel lorem porta ultricies. Etiam ut egestas lectus. Cras tempus mi ex, eu ultricies quam sagittis vitae. Curabitur vel massa erat. Donec sed faucibus justo. Ut feugiat justo quam, sed porta felis pellentesque sit amet. Vivamus nisi dui, venenatis a nibh vel, semper consequat metus. Quisque porta posuere enim, in accumsan massa. Mauris bibendum, velit sit amet dapibus elementum, lacus libero tempor erat, ac cursus ex metus non ex. Nullam consectetur, odio eget interdum imperdiet, eros neque dapibus neque, non semper enim diam sed nisi. Ut finibus nisi est, sed finibus est sodales at.Praesent vestibulum, massa vitae viverra tincidunt, lorem diam pretium ex, eu iaculis felis sem sit amet quam. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis nec aliquet enim. In elementum et turpis eget maximus. Donec sollicitudin lacus lectus, quis laoreet lacus blandit sed. In hac habitasse platea dictumst. Quisque quis bibendum massa. Donec cursus mauris tincidunt nisl congue, nec hendrerit ligula placerat. Sed at iaculis mi. Vestibulum vitae ante et nulla vestibulum vehicula. Vivamus ac felis eu diam hendrerit mattis. Praesent porta accumsan enim, eget eleifend lectus venenatis vitae. Duis commodo nisi tellus, non tristique massa pellentesque nec.Nullam eu mi facilisis, aliquam lectus vitae, viverra mauris. Morbi malesuada sem ipsum, at fermentum lectus commodo in. Suspendisse maximus, enim ac consectetur vehicula, lectus est elementum sem, vel pulvinar nulla lectus a sapien. Nam tincidunt laoreet elit nec placerat. Pellentesque porttitor, nisl ut dictum fringilla, lacus tellus rutrum ipsum, eget gravida velit lacus non arcu. Mauris sed faucibus nibh, sed iaculis ante. Ut lorem velit, aliquam scelerisque facilisis ac, scelerisque at felis. Quisque eleifend felis non purus molestie, vitae condimentum lectus consectetur.'
KL = get_random_bytes(16)
CIPHER = AES.new(KL, AES.MODE_ECB)
KRYPTO = CIPHER.encrypt(pad(W, 16))
# print(KRYPTO)
W2 = CIPHER.decrypt(KRYPTO)
print(W2)


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

KL_TAJNY = pow(int.from_bytes(KL, 'big'), e, n)

#ODBIORCA dostaje (KL_TAJNY, KRYPTO)
KLUCZ_2 = pow(KL_TAJNY, d, n).to_bytes(32, 'big')
# print(f"KLUCZ_2: {KLUCZ_2}")
CIPHER2 = AES.new(KLUCZ_2, AES.MODE_EAX, nonce=nonce)
W3 = CIPHER2.decrypt(KRYPTO)
print(f"odp: {unpad(W3, 16)}")














