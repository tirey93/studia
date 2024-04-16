# 3. Konwersja stopni Celsjusza na Fahrenheita i odwrotnie (funkcja)
#    convert_temp(type, value) gdzie type ma wartości małe lub duże 'F' or 'C'

def convert_temp(type, value):
    if type == 'F' or type == 'f':
        return (value * 1.8) + 32
    if type == 'C' or type == 'c':
        return (value - 32) * 5/9
    else:
        print('Niepoprawna wartosc typu')

print(convert_temp('C', 56.7))
print(convert_temp('F', 5.89))
print(convert_temp('c', 56.7))
print(convert_temp('f', 5.89))
print(convert_temp('x', 8))

