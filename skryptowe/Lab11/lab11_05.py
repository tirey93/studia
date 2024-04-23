# 5. Napisać skrypt, który pobierze i wyświetli wszystkie krotki z tabeli EMPLOYEES.
import sqlite3
with sqlite3.connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute("""
                 SELECT * FROM Employees
                 """)
    for row in cur.fetchall():
        print(row)