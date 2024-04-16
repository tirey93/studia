# 2. Napisać funkcję countChar(filename_input), która zlicza:
#   - liczbę znaków w pliku,
#   - liczbę białych znaków w pliku (białe znaki to spacja, tabulator, znacznik końca wiersza),
#   Wynikiem funkcji jest tablica złożona z 2 liczb całkowitych po jednej dla wymienionych podpunktów.
import string
string.whitespace  # (białe znaki to spacja, tabulator, znacznik końca wiersza)

def count_char(filename:str):
    with open(filename,"r") as file:
        all = 0
        white = 0
        for line in file:
            all += len(line)
            white += line.count(' ') + line.count('\n') + line.count('\t')
        return [all, white]

res = count_char('Anna_play.txt')
print(res[0])
print(res[1])