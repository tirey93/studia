# 2. Utworzyć i nawiązać połączenie do bazy test.db w bieżącym katalogu:
# (można także skopiować wcześniej utworzoną bazę danych test.db)
import sqlite3
conn = sqlite3.connect('test.db')
print ("Połączenie z bazą danych - nawiązane");
conn.close()
print ("Połączenie z bazą danych - zakończone ");
