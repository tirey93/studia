# 2. Utworzyć klasę Employee, która dziedziczy po klasie Person
# i zawiera dodatkowy atrybut Age.
# Zdefiniuj metodę displayEmployee(), która wyświetla nazwę pracownika,
# pensję oraz wiek.

from lab12_01 import Person  # lub skopiować daną klasę z pliku lab12_01.py


class Employee(Person):
    pass


if __name__ == "__main__":
    input('press any key -- Employee')
