# 7. Liczenie wartości funkcji podanej z klawiatury np. (x*x+2x+4 lub 1/(x+1))(wykorzystać funkcję eval())
# oraz zapisanie do pliku binarnego wartości x (od 0 do 50 o kroku 0.1) oraz y .
# Następnie wyświetlamy dane z pliku binarnego.
import numpy as np

equation = input("Podaj funkcje z parametrem 'x': ")

floatlist = []
for i in range(50*10):
    x = i/10.0
    try:
        y = eval(equation)
    except ZeroDivisionError:
        break
    floatlist.append([x, y])

with open("function_7.dat","wb") as file:
    to_write = np.array( floatlist, np.float64)
    bytes = to_write.tobytes()
    file.write(bytes)
    
with open("function_7.dat","rb") as file:
    bytes = file.read()
    deserialized_bytes = np.frombuffer(bytes, dtype=np.float64)
    deserialized_x = np.reshape(deserialized_bytes, newshape=(len(deserialized_bytes) // 2, 2))
    print(deserialized_x)