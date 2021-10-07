"""
    Veti primi un input de la tastatura (input()). By default, orice input
    de la tastatura este ca si tip de date str (string).
    Inputul vostru va fi intotdeauna un numar intreg, deci trebuie sa il
    convertiti la int, iar dupa ce aveti inputul, trebuie sa afisati toate
    numerele impare pana la numarul respectiv.

    exemplu:
        Daca veti primi 6, veti afisa:
        1
        3
        5
        cate un singur numar pe linie.
"""
# Rezolvare

# In x vom salva valoarea care vine de la tastatura
x = input()

# Convertim valoare pe care o primim de la tastatura intr-un intreg
x = int(x)

# Parcugem numerele de la 0 la x si afisam toate numerele impare
for i in range(x+1):
    if i % 2 == 1:
        print(i)

