# 8. Obsługa błędu np. przy tworzeniu tabeli, która już istnieje
#	(bez IF NOT EXISTS w poleceniu CREATE TABLE)

import sqlite3
with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute("""
                 SELECT name FROM sqlite_master WHERE type='table' AND name='Employees';
                 """)
    if len(cur.fetchall()) > 0:
        print('Tabela już istnieje')
    else:
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