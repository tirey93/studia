import matplotlib.pyplot as plt


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
def show():
    plt.show()

def drawPoints(x, color):
    # Rysowanie punktów
    plt.scatter(x[:, 0], x[:, 1], color=color)

    # Siatka
    plt.grid(True)

    ax = plt.gca()  # Pobierz aktualne osie

    # Przesuń osie do punktu (0, 0)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    # Ukryj górną i prawą oś
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

def drawLine(x1, x2, fullRange):
    # Wyznaczenie współczynników a i b
    a = -x2 / x1
    b = x2

    # Zakres wartości x (lista) - np od -10 do 10
    startRange = fullRange[0] - 5
    endRange = fullRange[1] + 5
    x_list = [startRange + i * 0.1 for i in range((endRange - startRange)*10)]
    # Obliczenie wartości y (lista)
    y_list = [a * x + b for x in x_list]

    # Rysowanie prostej
    plt.plot(x_list, y_list)
