# 1. Zapisywanie sesji gry do pliku (np. rzucanie dwoma kostkami, aż wyrzucimy 6,6)
# dla danej osoby ilości rzutów w danej sesji, datę zapisania danych.
# Nazwa pliku to {player_name}_play.txt. Jeśli plik dla danej osoby nie istnieje to tworzymy go,
# jeśli plik istnieje to dopisujemy następną sesję do istniejącego pliku.
# Nazwę gracza podajemy z klawiatury za pomocą funkcji input().
    # Przykładowa zawartość pliku Anna_play.txt:
    # Anna; 2023-11-22 13:23:23; Wyrzucono 6 i 6! po; 7; rzutach.
    # Anna; 2023-11-24 11:43:53; Wyrzucono 4 i 6! po; 12; rzutach.
# Tworzymy funkcje:
# play(dice1=6, dice2=6), która zwraca po ilu rzutach wyrzucono konkretne wartości kości jako listę np. result,
#    (defaultowo są ustawione na 6, ale można te watości zmienić, kolejność wyrzucenia nie ma znaczenia).
#    Funkcja zwraca, także dice1 i dice2, które wykorzystamy do zapisania danych do pliku.
# write_sesion_to_file(player_name, result), która zapisuje dane do pliku,
#    oraz
# funkcję read_session_file(player_name), która odczytuje dane z pliku.

import datetime
import random
class Result:
    position:int
    player:str
    date:datetime.datetime
    message:str
    tosses:int
    
    def display(self):
        v = f"{self.position};{self.player};{self.date.strftime('%Y-%m-%d %H:%M:%S')};{self.message};{self.tosses}; rzutach."
        print(v)
        return v

def from_line(line:str):
        result = Result()
        splitted = line.split(";")

        result.position = int(splitted[0])
        result.player = splitted[1]
        result.date = datetime.datetime.strptime(splitted[2], "%Y-%m-%d %H:%M:%S")
        result.message = splitted[3]
        result.tosses = int(splitted[4])
        return result

def play(dice1:int, dice2:int, player:str):
    tosses = 1

    toss1 = random.randrange(dice1) + 1
    while(toss1 != dice1):
        toss1 = random.randrange(6) + 1
        tosses += 1
    toss2 = random.randrange(dice2) + 1
    while(toss2 != dice2):
        toss2 = random.randrange(6) + 1
        tosses += 1
    result = Result()
    result.player = player
    result.position = 0
    result.date = datetime.datetime.now()
    result.message = f"{dice1} i {dice2}! po"
    result.tosses = tosses
    return result

def write_sesion_to_file(result:Result):
    with open(f"{result.player}_play.txt","a+") as file:
        file.write(f"{result.display()}\n")
def read_session_file(player_name):
    with open(f"{player_name}_play.txt","r") as file:
        print(''.join([line for line in file]))
# res = play(6,6, "Hubert")
# write_sesion_to_file(res)
# read_session_file("Hubert")

