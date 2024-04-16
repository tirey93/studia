# 2. Konwersja kilometry na mile i odwrotnie.
#    W programie wybieramy w pętli aż podamy poprawny wybór np.
#    'Podaj typ konwersji [km->mile]- 0, [mile->km]-1'.
#    Na tej podstawie wykonujemy funkcje wcześniej zdefiniowaną
#    km_mile(distance) lub mile_km(distance)

def km_mile(distance):
    conv_fac = 0.621371
    return distance * conv_fac
def mile_km(distance):
    conv_fac = 1.6
    return distance * conv_fac

choose = input('Podaj typ konwersji [km->mile]- 0, [mile->km]-1: ')
while choose != '1' and choose != '0':
    choose = input('Podaj typ konwersji [km->mile]- 0, [mile->km]-1: ')

try:
    distance = float(input('Podaj dystans: '))
except:
    distance = None
while distance is None:
    try:
        distance = float(input('Podaj dystans: '))
    except:
        distance = None
if choose == '1':
    print(km_mile(int(distance)))
else:
    print(mile_km(int(distance)))