# Napisz wyrażenie regularne do sprawdzania
# czy dana liczba jest liczbą ósemkową czy szesnastkową (tylko pełne dopasowanie)
# Dana liczba może być zarówno liczbą ósemkową i szesnastkową.
# Podaj ich odpowiednik dziesiętny.
import re
number = "0xfd899eec"

# h = "0xfd899eec"
# o = "0o37542317354"

h_re = re.fullmatch("0x[A-F0-9]+$", number, flags=re.IGNORECASE)
o_re = re.fullmatch("0o[0-8]+$", number, flags=re.IGNORECASE)

if h_re:
    print(f"Szesnastkowa: {int(number, 16)}")
if o_re:
    print(f"Ósemkowa: {int(number, 8)}")


# print(hex(number))
# print(oct(number))
