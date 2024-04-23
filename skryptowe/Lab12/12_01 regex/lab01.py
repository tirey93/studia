# Sprawdź czy dowolny kod pocztowy jest poprawny.
# (poza kodem nic nie może się pojawiać w zmiennej o nazwie kod,
# np. jeśli kod = '45-51711' lub kod = '145-517'
# to wynik poprawności kodu jest negatywny)
import re

kod = '45-517'
wynik = re.match('[0-9][0-9]-[0-9][0-9][0-9]', kod)
# wynik = re.match('[0-9]{2}-[0-9]{3}', kod)
# wynik = re.match('\d{2}-\d{3}', kod)
# czym się różni re.match od re.fullmatch czy re.search?
# Wykorzystaj każdą z funkcji i sprawdź ich działanie.

if wynik:
    print('Ok')
    print(wynik.group())
    print(kod)
else:
    print('No')

# Zdefiniuj funkcję is_valid_postal_code(postal_code)
# do sprawdzenia poprawności kodu (funkcja zwraca True lub False)