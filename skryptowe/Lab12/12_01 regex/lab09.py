# Napisz wyrażenie regularne do sprawdzenia wymagań co do hasła,
# gdzie spełnione są wszystkie poniższe warunki:

# hasło musi zawierać 1 cyfrę (0-9)
# hasło musi zawierać 1 wielką literę
# hasło musi zawierać 1 małą literę
# hasło musi zawierać 1 liczbę inną niż alfanumeryczna
# hasło składa się z 8-16 znaków bez spacji

# Przy sprawdzaniu podajemy co w kolejności od góry nie zostało jeszcze spełnione
# aż podamy hasło, które spełnia wszystkie wymogi.

import re
password = "haSlo1%&"

match_digit = re.findall("[0-9]", password)
match_upper = re.findall("[A-Z]", password)
match_lower = re.findall("[a-z]", password)
match_other = re.findall("[%&.!,?<>();:'\"|/@#$^*-]", password)
match_spaces = re.findall(" ", password)

if (len(match_digit) != 0
    and len(match_upper) != 0
    and len(match_lower) != 0
    and len(match_other) != 0
    and len(match_spaces) == 0
    and len(password) >= 8
    and len(password) <= 16 ):
    print("Haslo poprawne")
else:
    print("Haslo nie poprawne")

    print(f"Lenght: {len(password)}")
    print(f"digits: {len(match_digit)}")
    print(f"upper: {len(match_upper)}")
    print(f"lower: {len(match_lower)}")
    print(f"other: {len(match_other)}")
    print(f"spaces: {len(match_spaces)}")