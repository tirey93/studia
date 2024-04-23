# 3. W bazie danych test.db założyć tabelę (na podstawie materiałów z wykładów):
#   EMPLOYEES z kolumnami:
#   - ID
# 	- NAME
# 	- AGE
# 	- ADDRESS
# 	- SALARY
#   Zaproponować właściwe typy danych w każdej z kolumn dla bazy sqlite.

import sqlite3
with sqlite3.connect('test.db') as conn:
    conn.execute("""
                 CREATE TABLE "Employees" (
                    "id"	INTEGER,
                    "name"	TEXT,
                    "age"   NUMERIC,
                    "address" TEXT,
                    "salary" NUMERIC,
                    PRIMARY KEY("id")
                )
                 """)