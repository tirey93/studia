# Sprawdź czy adres email jest poprawny.
# Sprawdzić czy email postaci student@p.lodz.pl oraz student@p..pl
# jest poprawny (jeśli nie, to poprawić wyrażenie regularne)
import re

email = 'a1_f@wp.pl'
wynik = re.match(r'^[A-Z0-9._+%-]+@[A-Z0-9-.]+\.[A-Z]{2,}$', email, re.IGNORECASE)

if wynik:
    print('Ok')
    print(wynik.group())
else:
    print('No')
