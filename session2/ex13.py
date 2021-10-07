"""
    Veti primi 2 numere intregi de la tastatura (x si y).
    Va trebui sa le convertiti si apoi sa printati valorea lui x la puterea y.

    exemplu:
        Veti primi: 2 si 3
        Veti printa: 8
"""


x = input()
y = input()
x = int(x)
y = int(y)

# Functia pow returneaza valoarea lui x la puterea y
print(pow(x, y))
