# 4. Do tabeli: EMPLOYEES wprowadzić 3-4 krotki (rekordy).

import sqlite3
with sqlite3.connect('test.db') as conn:
    conn.execute("""
                 INSERT into Employees VALUES (1, 'Emp1', 12, 'address1', 12.5)
                 """)
    conn.execute("""
                 INSERT into Employees VALUES (2, 'Emp2', 25, 'address2', 13.54)
                 """)
    conn.execute("""
                 INSERT into Employees VALUES (3, 'Emp3', 56, 'address3', 0.23)
                 """)