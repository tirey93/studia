zoo = ["lion", "elephant", "monkey"]
# Zapisz każdy element listy w nowej linijce w pliku output.txt

# if __name__ == "__main__":
#     f = open("output.txt", 'w')

#     for i in zoo:
#         f.write(i+'\n')          # dodaj po kolei każdy element tablicy do pliku
#     f.close()                    # zamknij plik

# Powtórzyć rozwiązanie z wykorzystaniem składni with i dodaj modyfikator 'a'
with open("output.txt", "a") as file:
    for i in zoo:
        file.write(i+'\n')