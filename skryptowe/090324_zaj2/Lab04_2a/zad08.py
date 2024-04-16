# 8. Liczymy całkę z funkcji podanej na stałe np. y = 2*x**2+x-6 lub y = sin x.
#    Podajemy jednoczesnie wartość x początkową, wartość x końcową i krok całkowania.
#    Sprawdzić różnicę przy podaniu różnych kroków całkowania.
def funkcja(x):
    return 2*x**2+x-6


def metoda_trapezow(a, b, n):
    integral = 0

    dx = (b - a) / n

    for i in range(n):
        fa = a + dx*i
        fb = a + dx*(i + 1)

        integral += (funkcja(fa) + funkcja(fb)) / 2*dx
    return integral


print(metoda_trapezow(0.0, 1.0, 10))
print(metoda_trapezow(0.0, 1.0, 100))
print(metoda_trapezow(0.0, 1.0, 1000))