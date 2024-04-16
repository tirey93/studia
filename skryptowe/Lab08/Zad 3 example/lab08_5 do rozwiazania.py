# 8.5. Zdefiniuj słownik podając firstName, lastName i studentID i zapisz do pliku dane1.json.
# Wykorzystaj moduł json i metodę dump(do zapisnia) i load(do pobrania danych w formacie json).
# Wyświetl istniejące dane w pętli o klucz - wartość.

import json

def dane_json(imie, nazwisko, indeks):
    return {'firstName': imie, 'lastName': nazwisko, 'studentID': indeks}

# Zapisz dany słownik (json) do pliku
# with open('dane.json', 'w') as json_file:
#     json.dump(dane_json('Piotr','Nowak', 234356), json_file, indent=2)

# Odczytaj dane z pliku json
pass

with open('dane.json', 'r') as json_file:
    res = json.load(json_file)
    print(res["firstName"])
    print(res["lastName"])
    print(res["studentID"])