# 8.2 Wypisz  linie komentarza z wykorzytsaniem utf-8
# encoding="utf-8"

with open("dane.dat","r") as file:
    while 1:
        line = file.readline()
        if not line: break
        if line[0] == "#":
            print(line, end='')
