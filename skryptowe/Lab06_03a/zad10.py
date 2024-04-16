# 10. Napisz prosty 'System ekspertowy', który określi czy dana osoba choruje
# na grypę czy przeziębienie
# w zależności od symptomów. Jeśli mamy wszystkie trzy symptomy: gorączka, ból mieśni
# i osłabienie to mamy grypę. Jeśli mamy gorączkę i osłabienie to przeziębienie,
#  jeśli tylko osłabienie to wszystko OK, a jeśli ból mieśni to jesteśmy przetrenowani.


from enum import Enum


class Symptom(Enum):
    GORACZKA = 1
    BOL_MIESNI = 2
    OSLABIENIE = 3

    def Na_co_chorujesz(symptomy: list):

        if (Symptom.GORACZKA in symptomy
                and Symptom.OSLABIENIE in symptomy
                and Symptom.BOL_MIESNI in symptomy):
            print("grypa")
        elif (Symptom.GORACZKA in symptomy
              and Symptom.OSLABIENIE in symptomy):
            print("przeziebienie")
        elif (Symptom.OSLABIENIE in symptomy):
            print("wszystko ok")
        elif (Symptom.BOL_MIESNI in symptomy):
            print("przetrenowanie")
        else:
            print("co innego")


print(Symptom.GORACZKA)
Symptom.Na_co_chorujesz([Symptom.BOL_MIESNI])
Symptom.Na_co_chorujesz([Symptom.OSLABIENIE, Symptom.GORACZKA])
