import math
import random

import sympy
from Crypto.Hash import MD5

wiad = "moja wiadomosc 124"
H = MD5.new()
H.update(bytes(wiad, 'UTF-8'))
hash = H.hexdigest()
print(f"nadawca hash: {hash}")