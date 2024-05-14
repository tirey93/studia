# 7. Napisać skrypt, który usunie z tabeli EMPLOYEES rekordy o ID <=2 (polecenie DELETE)


import sqlite3
with sqlite3.connect('test.db') as conn:
    conn.execute("""
                 DELETE FROM Employees WHERE id <= 2
                 """)