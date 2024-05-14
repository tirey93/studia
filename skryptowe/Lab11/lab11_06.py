# 6. Napisać skrypt, który zmodyfikuje składowane w tabeli EMPLOYEES dane
# (polecenie UPDATE) zwiększając o 10% wartość SALARY (dla wszystkich osób)

import sqlite3
with sqlite3.connect('test.db') as conn:
    conn.execute("""
                 UPDATE Employees set Salary = Salary * 1.1
                 """)