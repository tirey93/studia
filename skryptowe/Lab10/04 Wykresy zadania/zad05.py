# Utwórz diagram z ilością ocen wygenerowanych losowo z tablicy
# tab = ['2.0','3.0','3.5','4.0','4.5','5.0']
# lub tab = [2.0,3.0,3.5,4.0,4.5,5.0]
# Generujemy 100 ocen.
import matplotlib.pyplot as plt
from random import randrange

tab =    [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
grades = [0, 0, 0, 0, 0, 0]

for i in range(100):
    index = randrange(len(tab))
    grades[index] += 1
print(grades)

plt.bar(tab, grades, label='Ocena')
plt.show()