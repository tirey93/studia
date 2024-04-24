# Napisz definicję funkcji is_valid_license_plate(license_plate)
# z wykorzystaniem wyrażenia regularnego do sprawdzenia poprawnoścci
# tablic rejestracyjnych z Łodzi np. EL 45JK3.
# Funkcja zwraca True lub False.
import re



def is_valid_license_plate(license_plate):
    match = re.fullmatch("EL [A-Z0-9]{5}", license_plate)
    if match:
        return True
    return False

print(is_valid_license_plate("EL 45JK3"))
print(is_valid_license_plate("EL 45JK3X"))
print(is_valid_license_plate("EX 45JK3"))