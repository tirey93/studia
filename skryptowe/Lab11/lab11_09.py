# 9. Utworzyć w pamięci RAM tabelę z autonumeracją pola ID.
# conn = sqlite3.connect(':memory:')
# Zrealizować wstawianie danych na podstawie listy (tuple).
# Dodatkowo wstawianie i prezentacja danych powinna być zrealizowana na podstawie opracowanej do tego funkcji.
# Opracowane funkcje mają przyjmować określone atrybuty w zależności od ich przeznaczenia.
# Zaprezentować prawidłowe działanie tych funkcji
import sqlite3

conn = sqlite3.connect(':memory:')
def czytaj_dane():
    cur = conn.cursor()
    cur.execute("""
                 SELECT * FROM EMPLOYEES
                 """)
    for row in cur.fetchall():
        print(row)
def utworz_tabele():
    conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
    (
    ID INTEGER,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL,
    PRIMARY KEY("ID" AUTOINCREMENT))''')
def wstaw_dane(lista):
    for row in lista:
        conn.execute(f"""
                    INSERT into Employees VALUES (NULL,'{row[0]}', {row[1]}, '{row[2]}', {row[3]})
                    """)

utworz_tabele()
wstaw_dane([
    ["emp1", 34, "address1", 23.76],
    ["emp1", 34, "address1", 23.76],
    ["emp1", 34, "address1", 23.76]])
czytaj_dane()