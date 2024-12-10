import matplotlib.pyplot as plt


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
    x_list = [fullRange[0] + i * 0.1 for i in range((fullRange[1] - fullRange[0])*10)]
    # Obliczenie wartości y (lista)
    y_list = [a * x + b for x in x_list]

    # Rysowanie prostej
    plt.plot(x_list, y_list)
