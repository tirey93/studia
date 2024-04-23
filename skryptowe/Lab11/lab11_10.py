# 10. Ostatni przykład, wstawić powyższe 3 funkcje do oddzielnego modułu modul_db.py
#   oraz wykonać powyższe funkcje (pamiętajmy, iż zmienna conn jest dostępna w ramach jedengo skryptu.
#   Jednak gdy przeniesiemy je do oddzielnego modułu to parametrem wejściowym powinna być zmienna conn)

import sqlite3
import modul_db

conn = sqlite3.connect(':memory:')
modul_db.utworz_tabele(conn)
modul_db.wstaw_dane([
    ["emp1", 34, "address1", 23.76],
    ["emp1", 34, "address2", 23.76],
    ["emp1", 34, "address1", 23.76]], conn)
modul_db.czytaj_dane(conn)