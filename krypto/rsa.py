import math

def my_gcd(n1:int, n2:int):
    if n1 == n2:
        return n1
    
    if n1 > n2:
        return my_gcd(n1 - n2, n2)
    return my_gcd(n2 - n1, n1)
    
def find_mod_inf(a:int, b:int):
    for i in range(b):
        if i * a % b == 1:
            return i

# print(my_gcd(1013,177))
# print(find_mod_inf(177, 1013))
# print(1013 % 177)

# print(f"pow: {pow(177, -1, mod=1013)}")

msg = "hello!"
byt = msg.encode("ascii")
to_int = int.from_bytes(byt, byteorder="big")
# print(to_int)

byt_in = to_int.to_bytes(len(byt), byteorder="big")
msg_in = byt_in.decode(encoding="ascii")
# print(msg_in)

a = 12
b = 9

for i in range(a):
    print(i % b)