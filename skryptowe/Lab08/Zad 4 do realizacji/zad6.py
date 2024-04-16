# 6. Napisać funkcję find_word(filename_input, word),
# której zadaniem jest znalezienie wszystkich wierszy w pliku filename_in.txt, które zawierają szukane słowo.
# Wszystkie wiersze, które zawierają dane słowo powinny zostać zapisane w pliku wynikowym filnename_out.txt
# wraz z nr wiersza (z pierwszego pliku). Plik wejściowy to dowolny plik tekstowy.


def find_word(word:str):
    out = ""
    with open("filename_in.txt","r") as file_in:
        i = 0
        for line in file_in:
            if word in line:
                out += f"{i}\t{line}\n"
            i += 1
    with open("filename_out.txt","w") as file_out:
        file_out.write(out)

find_word("word")