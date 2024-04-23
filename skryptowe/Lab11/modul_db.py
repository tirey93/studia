def czytaj_dane(connection):
    cur = connection.cursor()
    cur.execute("""
                 SELECT * FROM EMPLOYEES
                 """)
    for row in cur.fetchall():
        print(row)
def utworz_tabele(connection): #gotowa funkcja
    connection.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
    (ID INTEGER PRIMARY KEY ASC,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL);''')
def wstaw_dane(lista,connection):
    for row in lista:
        connection.execute(f"""
                    INSERT into Employees VALUES (NULL,'{row[0]}', {row[1]}, '{row[2]}', {row[3]})
                    """)
